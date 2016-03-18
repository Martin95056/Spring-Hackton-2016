package GUI;

import java.awt.Dimension;
import java.awt.Image;
import java.awt.Toolkit;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class BotCardsDrawer {

	private JFrame frame;
	private JPanel contentPanel;
	private int drawX, drawY;
	private int cardWidth, cardHeigth;
	private ImageIcon defaultImage = null;
	private ImageIcon defaultReversedImage = null;

	public BotCardsDrawer(JFrame frame, JPanel panel) {
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		cardWidth = (int) screenSize.getWidth() / 15;
		cardHeigth = (int) screenSize.getHeight() / 8;
		try {
			File imageFile = new File(
					"src/card-BMPs/"
							+ "A" + "Spades" + ".bmp");
			defaultImage = new ImageIcon(ImageIO.read(imageFile)
					.getScaledInstance(cardWidth, cardHeigth,
							Image.SCALE_SMOOTH));
			defaultReversedImage = new ImageIcon(ImageIO.read(imageFile)
					.getScaledInstance(cardHeigth, cardWidth,
							Image.SCALE_SMOOTH));

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.frame = frame;
		this.contentPanel = panel;

		resetDrawCoordinates();

	}
	private void resetDrawCoordinates()
	{
		drawX = cardWidth * 2;
		drawY = 0;
	}

	public void drawTopBotCards(int cardsNumber) {
		drawX+=cardWidth;
		for (int i = 0; i < cardsNumber; i++) {
			drawCard(false);
			drawX += cardWidth + 15;
		}
		resetDrawCoordinates();
	}

	public void drawLeftBotCards(int cardsNumber) {
		drawX = cardWidth;
		for (int i = 0; i < cardsNumber; i++) {
			drawCard(true);
			drawY += cardHeigth + 15;
		}
		resetDrawCoordinates();
	}

	public void drawRightBotCards(int cardsNumber) {
		drawX = (int) (Toolkit.getDefaultToolkit().getScreenSize().getWidth() - drawX);
		for (int i = 0; i < cardsNumber; i++)
		{
			drawCard(true);
			drawY += cardHeigth + 15;
		}
		resetDrawCoordinates();

	}

	private void drawCard(boolean reversed) {
		JLabel defaultCardLabel;
		if (reversed)
			defaultCardLabel = new JLabel(defaultReversedImage);
		else
			defaultCardLabel = new JLabel(defaultImage);
		defaultCardLabel.setBounds(drawX, drawY, cardWidth, cardHeigth);
		defaultCardLabel.setVisible(true);
		contentPanel.add(defaultCardLabel);
		frame.pack();

	}

}
