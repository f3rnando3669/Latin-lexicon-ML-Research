package NLP_Pipeline;

import com.robbinstony.nlp.Pipeline;
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

        Scanner scanner = new Scanner(new File("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//input.txt"));

        PrintWriter out = new PrintWriter("C://Users//apeng//IdeaProjects//NLP_Pipeline//src//main//java//NLP_Pipeline//output.txt");

        while(scanner.hasNextLine()){
            String input = scanner.nextLine();
            System.out.println("Input: " + input);

            String lemmaOutput = Lemma(input);
            System.out.println("Post-Lemma: " + lemmaOutput);

            String POSoutput = POS(lemmaOutput);
            System.out.println("Post-POS: " + POSoutput);

            String SRoutput = SentenceRecognizer(POSoutput);
            //System.out.println(SRoutput)    ;

            //String PatternMatchedOutput = PatternMatching(SRoutput);
            //System.out.println("Post-PatternMatching: " + PatternMatchedOutput);

            out.println("Input: " + input + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + POSoutput + "\nFinal Output: " + SRoutput);
        }
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

    public static String Lemma(String SRoutput){
        CoreDocument coreDocument = new CoreDocument(SRoutput);
        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();
        String[] words = new String[coreLabelList.size()];

        int i = 0;

        for(CoreLabel coreLabel : coreLabelList){
            words[i] = coreLabel.lemma();
            i++;
        }

        String output = String.join(" ", words);

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

        // PatternMatching() Flaws:
        // 1. It doesn't actually search through the given input. It is basically hard coded to find the patterns below,
        // so it is really dumb.
        // It should check each item in the input against the possible matching POS in a pattern sequence.

        // PatternMatchingHelper(): Good idea?
        // 1. Scans the input and hands a word at a time to a pattern matching method that will check if it starts or
        // continues a sequence, and determine where to go from there.


            String[] alphabet = new String[]{"DT", "NN", "NNP", "VBP", "JJ"};
            int currentState = 0;

            String[] words = POSoutput.split(" ");

            // C is for testing.
            String[] C = new String[]{"DT","NN", "NNP", "VBP", "JJ"};

            while(currentState != 6 && currentState != 7){

                if (C[0] == alphabet[0]) {
                    System.out.println("Found DT!");
                    currentState = 1;
                } else if (C[0] == alphabet[1]) {
                    System.out.println("Found NN!");
                    currentState = 3;
                } else if (C[1] == alphabet[1]) {
                    System.out.println("Found NN!");
                    currentState = 3;
                } else if (C[2] == alphabet[2]) {
                    System.out.println("Found NNP!");
                    currentState = 4;
                } else currentState = 7;

                if(currentState == 1){
                    if(C[1] == alphabet[1]){
                        System.out.println("Found NN after DT!");
                        currentState = 2;
                    } else currentState = 7;

                }
                if(currentState == 2){
                    if(C[2] == alphabet[2]){
                        System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;

                }
                if(currentState == 3){
                    if(C[2] == alphabet[2]){
                        System.out.println("Found VBP!");
                        currentState = 5;
                    } else if (C[1] == alphabet[2]) {
                        System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;

                }
                if(currentState == 4){
                    if(C[2] == alphabet[2]){
                        System.out.println("Found VBP!");
                        currentState = 5;
                    } else currentState = 7;

                }
                if(currentState == 5){
                    if(C[4] == alphabet[4] || C[4] == alphabet[1]){
                        System.out.println("Found NN or JJ!");
                        currentState = 6;
                    } else currentState = 7;
                }
            }

            if(currentState == 6){
                System.out.println("Pattern Match!");
                //System.out.println("The words in the sentence that are associated with the POS tags.");
            }

            if(currentState == 7){
                System.out.println("No pattern found.");
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
