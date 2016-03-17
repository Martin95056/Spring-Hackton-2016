package GUI;

import java.util.ArrayList;

import CardLogic.Card;
import CardLogic.CardSorter;

public class MainClass {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Card card = new Card("A", "Clubs");
		CardsDrawer CD = CardsDrawer.getInstance();
		ArrayList<Card> cards = new ArrayList<>();
		cards.add(new Card("A", "Clubs"));
		cards.add(new Card("J", "Clubs"));
		cards.add(new Card("9", "Clubs"));
		cards.add(new Card("10", "Clubs"));
		cards.add(new Card("8", "Clubs"));
		cards.add(new Card("Q", "Clubs"));
		cards.add(new Card("K", "Clubs"));
		cards.add(new Card("7", "Clubs"));
		CardSorter.sort(cards, "All Trumps");
		CD.drawCards(cards);
	}

}
