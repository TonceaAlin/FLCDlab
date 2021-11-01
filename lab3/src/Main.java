import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        run("p1err.txt");
    }

    private static void run(String filepath) {
        MyScanner scan = new MyScanner(filepath);
        try {
            scan.scan();
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
        toFile("ST.out", scan.getSymbolTable().stream().filter(x -> !x.isEmpty()).collect(Collectors.toList()));
        toFile("PIF.out", scan.getPIF().toString());
    }

    public static void toFile(String filepath, Object object){
        try (PrintStream printStream = new PrintStream(filepath)) {
            printStream.println(object);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
