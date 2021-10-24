import java.util.ArrayList;

public class SymbolTable {
    private ArrayList<ArrayList<String>> elements;
    private int capacity;

    public SymbolTable(int capacity) {
        this.capacity = capacity;
        this.elements = new ArrayList<>();
        for (int i = 0; i < capacity; i++) {
            this.elements.add(new ArrayList<>());
        }
    }

    public int add(String key){
        int search = search(key);
        if(search == -1) {
            int pos = this.hashFunction(key);
            this.elements.get(pos).add(key);
            return pos;
        }
        return search;
    }

    public int search(String key){
        int pos = this.hashFunction(key);
        if(this.elements.get(pos).contains(key)){
            return pos;
        }
        return -1;
    }

    private int hashFunction(String key){
        int asciiSum = 0;
        for(int index = 0; index < key.length(); index++){
            asciiSum += key.charAt(index);
        }
        return asciiSum % this.capacity;
    }
}
