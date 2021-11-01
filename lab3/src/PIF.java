import java.util.ArrayList;
import java.util.List;

public class PIF {
    private List<Pair<String, Integer>> tokensPositions;

    public PIF(){
        this.tokensPositions = new ArrayList<>();
    }

    public void add(Pair<String, Integer> element){
        this.tokensPositions.add(element);
    }

    public List<Pair<String, Integer>> get() {
        return this.tokensPositions;
    }

}
