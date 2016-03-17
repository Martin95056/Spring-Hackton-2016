package CardLogic;
import java.util.HashMap;

public class CardPairValues {

	private static HashMap<String, PairValues> map = null;
	private static CardPairValues instance = null;

	private CardPairValues() {
		map = new HashMap<>();
		map.put("J", new PairValues(20, 2));
		map.put("9", new PairValues(14, 0));
		map.put("A", new PairValues(11, 11));
		map.put("10", new PairValues(10, 10));
		map.put("K", new PairValues(4, 4));
		map.put("Q", new PairValues(3, 3));
		map.put("8", new PairValues(0, 0));
		map.put("7", new PairValues(0, 0));
	}

	public static CardPairValues getInstance() {
		if (instance == null) {
			instance = new CardPairValues();
		}
		return instance;
	}

	public HashMap<String, PairValues> getMap() {
		return map;
	}
}
