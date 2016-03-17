package CardLogic;
import static org.junit.Assert.*;

import java.util.ArrayList;

import org.junit.Before;
import org.junit.Test;

public class CardSorterTest {

	ArrayList<Card> cards = null;

	@Before
	public void initialize() {
		cards = new ArrayList<>();
		cards.add(new Card("A", "Hearts"));
		cards.add(new Card("J", "Hearts"));
		cards.add(new Card("9", "Hearts"));
		cards.add(new Card("10", "Spades"));
		cards.add(new Card("A", "Spades"));
		cards.add(new Card("7", "Clubs"));
		cards.add(new Card("9", "Clubs"));
		cards.add(new Card("J", "Clubs"));

	}

	@Test
	public void allTrumpsTest() {
		ArrayList<Card> expected = new ArrayList<>();
		CardSorter.sort(cards, "All Trumps");
		expected.add(new Card("J", "Clubs"));
		expected.add(new Card("9", "Clubs"));
		expected.add(new Card("7", "Clubs"));
		expected.add(new Card("J", "Hearts"));
		expected.add(new Card("9", "Hearts"));
		expected.add(new Card("A", "Hearts"));
		expected.add(new Card("A", "Spades"));
		expected.add(new Card("10", "Spades"));
		assertArrayEquals(expected.toArray(), cards.toArray());
	}

	@Test
	public void noTrumpsTest() {
		ArrayList<Card> expected = new ArrayList<>();
		CardSorter.sort(cards, "No Trumps");
		expected.add(new Card("J", "Clubs"));
		expected.add(new Card("9", "Clubs"));
		expected.add(new Card("7", "Clubs"));
		expected.add(new Card("A", "Hearts"));
		expected.add(new Card("J", "Hearts"));
		expected.add(new Card("9", "Hearts"));
		expected.add(new Card("A", "Spades"));
		expected.add(new Card("10", "Spades"));
		assertArrayEquals(expected.toArray(), cards.toArray());
	}

}
