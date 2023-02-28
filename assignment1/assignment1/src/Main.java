public class Main {
    public static void main(String[] args){
        CharacterCreator characterCreator = new CharacterCreator();
        Battle battle = new Battle();
        battle.twoOutOfThree(characterCreator.generateCharacter(), characterCreator.generateCharacter());
    }
}
