package CardLogic;
import java.io.File;

public class Main {

	public static void main(String[] args){
		System.out.println(JsonParser.getFirst5CardsFromJson(new File("C:/Users/ThinkPad/Documents/file.json")));
	}

}
