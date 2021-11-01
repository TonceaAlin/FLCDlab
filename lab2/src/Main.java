public class Main {
    public static void main(String[] args) {
        SymbolTable symbolTable = new SymbolTable(5);
        System.out.println(symbolTable.add("a"));
        System.out.println(symbolTable.add("bcd"));
        System.out.println(symbolTable.add("abdx"));
        System.out.println(symbolTable.add("a"));
        System.out.println("search");
        System.out.println(symbolTable.search("a"));
        System.out.println(symbolTable.search("bcd"));
        System.out.println(symbolTable.search("abdx"));
    }
}
