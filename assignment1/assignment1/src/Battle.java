import java.util.HashMap;
import java.util.Random;

public class Battle {
    public void twoOutOfThree(HashMap<String, String> player, HashMap<String, String> enemy){
        HashMap<String, Integer> results = new HashMap<>();
        int i = 1;
        while (true){
            String winner = runBattle(player, enemy);
            if (results.containsKey(winner)){
                int j = results.get(winner) + 1;
                results.put(winner, j);
            } else {
                results.put(winner, 1);
            } if (results.get(winner) >= 2){
                System.out.println(" ");
                System.out.println(winner + " is victorious after " + i + " battles!" );
                System.out.println(" ");
                System.out.println("------- Battle End -------");
                break;
            }
            i += 1;
        }
    }
    public String runBattle(HashMap<String, String> player, HashMap<String, String> enemy){
        Random rand = new Random();
        System.out.println("------- Let the Battle begin! ------");
        System.out.println(" ");
        String playerName = player.get("name");
        String playerWeapon = player.get("weaponName");
        String playerHealthString = player.get("health");
        String playerWeaponDamageString = player.get("weaponDamage");
        int playerHealth = Integer.parseInt(playerHealthString);
        int playerWeaponDamage = Integer.parseInt(playerWeaponDamageString);
        String enemyName = enemy.get("name");
        String enemyWeapon = enemy.get("weaponName");
        String enemyHealthString = enemy.get("health");
        String enemyWeaponDamageString = enemy.get("weaponDamage");
        int enemyHealth = Integer.parseInt(enemyHealthString);
        int enemyWeaponDamage = Integer.parseInt(enemyWeaponDamageString);
        System.out.println(playerName + " draws their " + playerWeapon);
        System.out.println(enemyName + " draws their " + enemyWeapon);
        System.out.println(" ");
        int i = 0;
        while (playerHealth > 0 & enemyHealth > 0){
            if (i % 2 == 0){
                int playerAttack = rand.nextInt(0, playerWeaponDamage);
                enemyHealth -= playerAttack;
                System.out.println(playerName + " attacks " + enemyName + " with their " + playerWeapon + " for " + playerAttack + " damage");
                System.out.println(enemyName + " HP = " + enemyHealth);
            } else {
                int enemyAttack =  rand.nextInt(0, enemyWeaponDamage);
                playerHealth -= enemyAttack;
                System.out.println(enemyName + " attacks " + playerName + " with their " + enemyWeapon + " for " + enemyAttack + " damage");
                System.out.println(playerName + " HP = " + playerHealth);
            }
            i += 1;
            System.out.println(" ");
        }
        if (playerHealth <= 0){
            System.out.println(playerName + "is defeated");
            System.out.println(" ");
            return enemyName;
        } else {
            System.out.println(enemyName + "is defeated");
            System.out.println(" ");
            return playerName;
        }
    }
}
