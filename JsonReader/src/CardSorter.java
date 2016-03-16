import java.util.ArrayList;
import java.util.Comparator;

public class CardSorter {

	private static void trumpSort(ArrayList<Card> cards) {
		Comparator<Card> trumpCompare = new Comparator<Card>() {

			@Override
			public int compare(Card firstCard, Card secondCard) {

				if (firstCard.getTrumpValue() < secondCard.getTrumpValue())
					return 1;
				else if (firstCard.getTrumpValue() == secondCard.getTrumpValue())
					return 0;
				else
					return -1;
			}

		};
		cards.sort(trumpCompare);
	}

	private static void nonTrumpSort(ArrayList<Card> cards) {
		Comparator<Card> nonTrumpCompare = new Comparator<Card>() {

			@Override
			public int compare(Card firstCard, Card secondCard) {
				if (firstCard.getNonTrumpValue() < secondCard.getNonTrumpValue())
					return 1;
				else if (firstCard.getNonTrumpValue() == secondCard.getNonTrumpValue())
					return 0;
				else
					return -1;
			}

		};
		cards.sort(nonTrumpCompare);
	}
	//Splits the cards into 4 arrays (clubs, diamonds, hearts, spades)
	private static ArrayList<ArrayList<Card>> splitInSuits(ArrayList<Card> cards) {
		ArrayList<Card> clubs = new ArrayList<Card>();
		ArrayList<Card> diamonds = new ArrayList<Card>();
		ArrayList<Card> hearts = new ArrayList<Card>();
		ArrayList<Card> spades = new ArrayList<Card>();
		for (Card c : cards) {
			if (c.getSuit().equals("Clubs"))
				clubs.add(c);
			else if (c.getSuit().equals("Diamonds"))
				diamonds.add(c);
			else if (c.getSuit().equals("Hearts"))
				hearts.add(c);
			else
				spades.add(c);
		}
		ArrayList<ArrayList<Card>> splittedArrays = new ArrayList<>();
		splittedArrays.add(clubs);
		splittedArrays.add(diamonds);
		splittedArrays.add(hearts);
		splittedArrays.add(spades);
		return splittedArrays;
	}

	private static void trumpCardsSorter(ArrayList<Card> cards) {

		ArrayList<ArrayList<Card>> splitted = splitInSuits(cards);
		cards.clear();
		for (ArrayList<Card> list : splitted) {
			trumpSort(list);
			cards.addAll(list);
		}

	}
	private static void eightCardsSorter(ArrayList<Card> cards, String contract) {
		ArrayList<ArrayList<Card>> splitted = splitInSuits(cards);
		cards.clear();
		int contractInt = 0;
		if (contract.equals("No Trumps"))
			contractInt = 5;
		else if (contract.equals("Clubs"))
			contractInt = 0;
		else if (contract.equals("Diamonds"))
			contractInt = 1;
		else if (contract.equals("Hearts"))
			contractInt = 2;
		else
			contractInt = 3;
		int splittedIterator = 0;
		for (ArrayList<Card> list : splitted) {
			if (splittedIterator == contractInt) {
				trumpSort(list);
				cards.addAll(list);
			} else {
				nonTrumpSort(list);
				cards.addAll(list);
			}
			splittedIterator++;
		}
	}
	//By default (if no contract is present) sorts the cards as if the contract is All Trumps
	public static void sort(ArrayList<Card> cards) {

		trumpCardsSorter(cards);

	}
	
	public static void sort(ArrayList<Card> cards, String contract) {
		if (contract.equals("All Trumps"))
			trumpCardsSorter(cards);
		else
			eightCardsSorter(cards, contract);

	}

}