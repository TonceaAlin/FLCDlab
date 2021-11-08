import java.util.ArrayList;
import java.util.List;

public class PIF {
    public List<Pair<String, Integer>> tokensPositions;

    public PIF(){
        this.tokensPositions = new ArrayList<>();
    }

    public void add(Pair<String, Integer> element){
        this.tokensPositions.add(element);
    }

    public String get() {
        return this.tokensPositions.toString();
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (Pair<String, Integer> tokensPosition : this.tokensPositions) {
            stringBuilder.append(tokensPosition.getFirst())
                    .append(" : ")
                    .append(tokensPosition.getSecond())
                    .append("\n");
        }
        return stringBuilder.toString();
    }
}
