import java.io.IOException;
import java.io.FileReader;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileWriter;
public class process_wiki_txt {
    public static void main(String[] args) throws IOException {
        FileReader freader = new FileReader("wiki_snippet.txt");
        BufferedReader breader = new BufferedReader(freader);
        String readIntoString;
        //create the processed_wiki.txt file
        try {
            File myObj = new File("processed_wiki.txt");
            if (myObj.createNewFile()) {
                System.out.println("File created: " + myObj.getName());
            } else {
                System.out.println("File already exists");
            }
        } catch (IOException e) {
            System.out.println("Something gone wrong");
            e.printStackTrace();
        }

        while (breader.ready()) {
            readIntoString = breader.readLine();
            sentenceBreaker(readIntoString);
        }


    }

    public static void sentenceBreaker(String line) throws IOException{
        String fileAsString = line;
        FileWriter fileWriter= new FileWriter("processed_wiki.txt", true);
        int count = 0;
        for (int i = 0; i < fileAsString.length(); i++) {
            fileWriter.append(fileAsString.charAt(i));
            count++;
            //do not move to new line @ et al.
            if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'l') &&
                    (fileAsString.charAt(i - 2) == 'a') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ i.e.
            //i.e
            else if (((i-1) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'i') &&
                    (((i + 1) < (fileAsString.length() - 2)) && (fileAsString.charAt(i + 1) == 'e'))) {
                fileWriter.append("");
            }//.e.
            else if (((i-2) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'e') &&
                    (fileAsString.charAt(i - 2) == '.')) {
                fileWriter.append("");
            }//do not move to new line @ e.g.
            //e.g
            else if (((i-1) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'e') &&
                    (((i + 1) < (fileAsString.length() - 2)) && (fileAsString.charAt(i + 1) == 'g'))) {
                fileWriter.append("");
            }//.g.
            else if (((i-2) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'g') &&
                    (fileAsString.charAt(i - 2) == '.')) {
                fileWriter.append("");
            }//do not move to new line @ eq.
            else if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'q') &&
                    (fileAsString.charAt(i - 2) == 'e') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ st.
            else if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 't') &&
                    (fileAsString.charAt(i - 2) == 's') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ mr.
            else if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'r') &&
                    (fileAsString.charAt(i - 2) == 'm') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ ms.
            else if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 's') &&
                    (fileAsString.charAt(i - 2) == 'm') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ dr.
            else if (((i-3) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'r') &&
                    (fileAsString.charAt(i - 2) == 'd') &&
                    (fileAsString.charAt(i - 3) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ mrs.
            else if (((i-4) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 's') &&
                    (fileAsString.charAt(i - 2) == 'r') &&
                    (fileAsString.charAt(i - 3) == 'm') &&
                    (fileAsString.charAt(i - 4) == ' ')) {
                fileWriter.append("");
            }//do not move to new line @ etc.
            else if (((i-4) > 0) &&
                    (fileAsString.charAt(i) == '.') &&
                    (fileAsString.charAt(i - 1) == 'c') &&
                    (fileAsString.charAt(i - 2) == 't') &&
                    (fileAsString.charAt(i - 3) == 'e') &&
                    (fileAsString.charAt(i - 4) == ' ')) {
                fileWriter.append("");
            }//if decimals
            else if (((i + 1) < (fileAsString.length() - 2)) &&
                    (Character.isDigit(fileAsString.charAt(i))) &&
                    (fileAsString.charAt(i+1) == '.') &&
                    (Character.isDigit((fileAsString.charAt(i+2))))) {
                while (((i + 1) < (fileAsString.length() - 2)) && ((Character.isDigit(fileAsString.charAt(i + 2)))))
                {
                    fileWriter.append(fileAsString.charAt(i+1));
                    i++;
                }
            }//if 2x quotes
            else if ((fileAsString.charAt(i) == '\"')){
                fileWriter.append("");
                i++;
                while (((i + 1) < (fileAsString.length() - 2)) && (fileAsString.charAt(i) != '\"')){
                    fileWriter.append(fileAsString.charAt(i));
                    i++;
                }
                if(i < fileAsString.length()-2) {
                    fileWriter.append(fileAsString.charAt(i));
                }
                if((fileAsString.charAt(i-1) == '.') ||
                (fileAsString.charAt(i-1) == '?')||
                        (fileAsString.charAt(i-1) == '!')){
                    fileWriter.append("\n");
                    while (((i + 1) < (fileAsString.length() - 2)) && ((!Character.isLetter(fileAsString.charAt(i + 1))) && (fileAsString.charAt(i + 1) != '\"')))
                        i++;
                }
            }//if parentheses
            else if ((fileAsString.charAt(i) == '(')){
                fileWriter.append("");
                i++;
                while (((i + 1) < (fileAsString.length() - 2)) && (fileAsString.charAt(i) != ')')){
                    fileWriter.append(fileAsString.charAt(i));
                    i++;
                }
                if(i < fileAsString.length()-2) {
                    fileWriter.append(fileAsString.charAt(i));
                }
            }//if sentence ends with period
            else if((fileAsString.charAt(i) == '.')){
                fileWriter.append("\n");
                while (((i + 1) < (fileAsString.length() - 2)) && ((!Character.isLetter(fileAsString.charAt(i + 1))) && (fileAsString.charAt(i + 1) != '\"')))
                    i++;
            }// if sentence ends with question mark
            else if (fileAsString.charAt(i) == '?') {
                fileWriter.append("\n");
            }// if sentence ends with exclamation mark
            else if (fileAsString.charAt(i) == '!') {
                fileWriter.append("\n");
            }//filler else statement
            else {
                ;
            }
        }
        fileWriter.close();
    }
}



