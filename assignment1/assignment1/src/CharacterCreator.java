import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.HashMap;

public class CharacterCreator {
    public  HashMap<String, String> generateCharacter(){
        Random rand = new Random();
        int healthInt = rand.nextInt(25, 35);
        String health = String.valueOf(healthInt);
        HashMap<String, String> playerCharacter = new HashMap<>();
        playerCharacter.put("name", generateName());
        playerCharacter.put("health", health);
        String[] weaponAndDamage = generateWeapon().split(" ");
        playerCharacter.put("weaponName", weaponAndDamage[0]);
        playerCharacter.put("weaponDamage", weaponAndDamage[1]);
        return playerCharacter;
    }
    public String generateName(){
        Random rand = new Random();
        ArrayList<String> nameArray = getFileContentsArray("resources/names.txt");
        int upperBoundNames = nameArray.size();
        String charName = nameArray.get(rand.nextInt(upperBoundNames));
        ArrayList<String> titleArray = getFileContentsArray("resources/titles.txt");
        int upperBoundTitles = titleArray.size();
        String charTitle = titleArray.get(rand.nextInt(upperBoundTitles));
        return (charName + " " + charTitle);
    }
    public String generateWeapon(){
        Random rand = new Random();
        ArrayList<String> weaponArray = getFileContentsArray("resources/weapons.txt");
        int upperBoundWeapons = weaponArray.size();
        return weaponArray.get(rand.nextInt(upperBoundWeapons));
    }
    public ArrayList<String> getFileContentsArray(String fileName) {
        try {
            File File = new File(fileName);
            Scanner scanner = new Scanner(File);
            ArrayList<String> fileContents = new ArrayList<>();
            while (scanner.hasNextLine()) {
                fileContents.add(scanner.nextLine());
            }
            return fileContents;
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            return null;
        }
    }
}
