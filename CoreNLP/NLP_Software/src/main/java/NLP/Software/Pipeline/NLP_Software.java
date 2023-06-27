package NLP_Pipeline;

import com.robbinstony.nlp.Pipeline;
import com.robbinstony.nlp.SentenceRecognizer;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.CoreSentence;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.simple.Sentence;
//import edu.stanford.nlp.naturalli.VerbTense;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.*;

public class NLP_Pipeline {
    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    public static void main(String[] args) throws FileNotFoundException {



        // The following Scanner, named scanner, allows us to read the input.txt file.
        Scanner scanner = new Scanner(new File("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//GutenbergKingJamesBible.txt"));

        // The following PrintWriter, named out, allows us to create and print in the output.txt file.
        PrintWriter out = new PrintWriter("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//output.txt");

        // The following while loop ensures that the Scanner continues to scan until it has nothing to scan.
        while(scanner.hasNextLine()){
            // The following String, named input, is where each line from the Scanner will be stored.
            String input = scanner.nextLine();

            String lemmaOutput = Lemma(input);

            String POSoutput = POS(lemmaOutput);

            String SRoutput = SentenceRecognizer(POSoutput);

            String PatternMatchedOutput = PatternMatching(SRoutput);
            // the following prints the String named lemmaOutput.

            out.println(PatternMatchedOutput);
        }
        // The following two lines shutdown or close the scanner and output to
        scanner.close();
        out.close();

    }

    public static String SentenceRecognizer(String input){
        CoreDocument coreDocument = new CoreDocument(input);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreSentence> sentences = coreDocument.sentences();

        StringBuilder output = new StringBuilder();
        for (CoreSentence sentence : sentences){
            output.append(sentence.toString()).append("\n");
        }
        return output.toString();
    }

    // The following is the Lemma method that runs the input through the Lemma process of NLP.
    public static String Lemma(String SRoutput){
        CoreDocument coreDocument = new CoreDocument(SRoutput);
        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];

        int i = 0;

        // The following for loop Lemma's each element in the array words. "i" is used to only run this as many times as needed, starting with the 0th element.
        for(CoreLabel coreLabel : coreLabelList){
            words[i] = coreLabel.lemma();
            i++;
        }
        // The following String formats the output with spaces between words, periods are words.
        String output = String.join(" ", words);
        // The following is self-explanatory. :)
        return output;
    }

    public static String POS(String Lemmaoutput){
        CoreDocument coreDocument = new CoreDocument(Lemmaoutput);
        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];

        int i = 0;

        for(CoreLabel coreLabel : coreLabelList){
            words[i] = coreLabel.get(CoreAnnotations.PartOfSpeechAnnotation.class);
            i++;
        }

        String output = String.join(" ", words);

        return output;
    }

    public static String PatternMatching(String POSoutput){

            String[] alphabet = new String[]{"DT", "NN", "NNP", "VBP", "JJ"};
            int currentState = 0;

            // This should split the sentence in output into individual words in an array.
            String[] words = POSoutput.split(" ");
            //System.out.println(words.length);

            // C is for testing.
            String[] C = new String[]{"DT", "NN", "NNP", "VBP", "JJ"};

            while(currentState != 6 && currentState != 7){
                if (C[0] == alphabet[0]) {
                    //System.out.println("Found DT!");
                    currentState = 1;
                } else if (C[1] == alphabet[1]) {
                    //System.out.println("Found NN!");
                    currentState = 3;
                } else if (C[2] == alphabet[2]) {
                    //System.out.println("Found NNP!");
                    currentState = 4;
                } else currentState = 7;
                // If the first tag is "DT", set currentState to 1.
                // Else if first tag is "NN", set currentState to 3.
                // Else if first tag is "NNP", set currentState to 4.
                if(currentState == 1){
                    if(C[1] == alphabet[1]){
                        //System.out.println("Found NN after DT!");
                        currentState = 2;
                    } else currentState = 7;
                    // If following the "DT" is "NN", set currentState to 2.
                }
                if(currentState == 2){
                    if(C[2] == alphabet[2]){
                        //System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;
                    // If the following is "VBP", set currentState to 5.
                }
                if(currentState == 3){
                    if(C[2] == alphabet[2]){
                        //System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;
                    // If the following is "VBP", set currentState to 5.
                }
                if(currentState == 4){
                    if(C[2] == alphabet[2]){
                        //System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;
                    //If the following is "VBP", set currentState to 5.
                }
                if(currentState == 5){
                    if(C[4] == alphabet[4]){
                        //System.out.println("Found NN or JJ!");
                        currentState = 6;
                    } else currentState = 7;
                    // If the following is "NN" or "JJ", set currentState to 6.
                }
            }
            if(currentState == 6){
                //System.out.println("Pattern Match!");
                //System.out.println("The words in the sentence that are associated with the POS tags.");
            }
            if(currentState == 7){
                //System.out.println("No pattern found.");
                return POSoutput;

            }
        return POSoutput;
    }

    public static int countSentences(String input){
        if(input == null || input.isEmpty()){
            return 0;
        }

        String[] sentences = input.split("[.]+");

        return sentences.length;
    }
}
