import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class MyScanner {
    private final String filepath;
    private final ArrayList<String> operators = new ArrayList<>(List.of("=","-","*","/","%","<","<=","=>","+",
            ">", "==", "!="));
    private final ArrayList<String> separators = new ArrayList<>(List.of("{","}","[","]","(",")","\n"," ", ".",";"));
    private final ArrayList<String> reservedWords = new ArrayList<>(List.of("read", "write", "var", "do_steps", "do_while", "test", "then", "else"
    ,"int", "and", "or", "char", "string"));
    private final PIF PIF;
    private final SymbolTable symbolTable;

    public MyScanner(String filepath) {
        this.filepath = filepath;
        this.PIF = new PIF();
        this.symbolTable = new SymbolTable(100);
    }
    public String readFile() throws FileNotFoundException {
        StringBuilder content = new StringBuilder();
        Scanner scanner = new Scanner(new File(this.filepath));
        while(scanner.hasNextLine()){
            content.append(scanner.nextLine()).append("\n");
        }
        return content.toString().replace("\t", "");
    }
    public void scan() throws FileNotFoundException {
        List<String> tokens = this.tokenize();
        for(String token: tokens){
            if(this.reservedWords.contains(token) || this.operators.contains(token) || this.separators.contains(token)){
                this.PIF.add(new Pair(token, -1));
            }else if(isIdentifier(token) || isConstant(token)){
                int pos = this.symbolTable.add(token);
                this.PIF.add(new Pair(token, pos));
            }else{
                System.out.println("lexical error");
            }
        }
    }

    List<String> tokenize() throws FileNotFoundException {
        String fileContent = this.readFile().replace("\t", "");
        String separators = this.separators.stream().reduce("", (a,b) -> a+b);
        List<String> tokensIncludingSeparators = Collections.list(new StringTokenizer(fileContent, separators, true)).stream()
                .map(token -> (String) token)
                .collect(Collectors.toList());
        for(String token : tokensIncludingSeparators){
            for(String operator : this.operators){
                if(token.contains(operator))
                {
                    for (int i = 0; i < token.length(); i++) {
                        if(isIdentifier(String.valueOf(token.charAt(i)))){
                            if(tokensIncludingSeparators.contains(token)){
                                tokensIncludingSeparators.set(tokensIncludingSeparators.indexOf(token), operator);
                            }
                        }
                    }
                }
            }
        }
        //System.out.println(tokensIncludingSeparators);
        return tokensIncludingSeparators;
    }

    public ArrayList<ArrayList<String>> getSymbolTable() {
        return this.symbolTable.get();
    }

    public List<Pair<String, Integer>> getPIF() {
        return this.PIF.get();
    }

    public boolean isIdentifier(String element){
        return element.matches("^[a-zA-Z_]([a-zA-Z0-9_]*)$");
    }

    public boolean isConstant(String element){
        return isCharacterConstant(element) || isStringConstant(element) || isNumericalConstant(element);
    }

    private boolean isNumericalConstant(String element) {
        return element.matches("^([1-9][0-9]*)|0$");
    }

    private boolean isStringConstant(String element) {
        return element.matches("^\"[a-zA-Z0-9 ]*\"$");
    }

    private boolean isCharacterConstant(String element) {
        return element.matches("^'[a-zA-Z0-9 ]'$");
    }

}
