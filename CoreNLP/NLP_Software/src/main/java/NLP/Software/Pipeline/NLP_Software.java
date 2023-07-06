package NLP.Software.Pipeline;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Scanner;

public class NLP_Software {

    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    public static void main(String[] args) throws FileNotFoundException {

        // Scanner reads from input.txt
        Scanner scanner = new Scanner(new File("C:/Users/sansk/IdeaProjects/NLP_Software/src/main/java/NLP/Software/Pipeline/input.txt"));

        // Creates an output.txt file to return outputs to
        PrintWriter out = new PrintWriter("C:/Users/sansk/IdeaProjects/NLP_Software/src/main/java/NLP/Software/Pipeline/output.txt");

        while (scanner.hasNextLine()) {
            // Reads each line of input
            String input = scanner.nextLine();

            // Separate the sentences
            String[] sentences = seperatedSentences(input);

            // Process each sentence individually
            for (String sentence : sentences) {
                String lemmaOutput = Lemma(sentence);

                String posOutput = POS(lemmaOutput);

                String patternMatchedOutput = PatternCheck(posOutput);

                out.println("Input: " + sentence + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + posOutput + "\nPattern Matching: " + patternMatchedOutput + "\nPattern Matched Output: " + "\n");

                // If you want to write the separated sentences to a file, uncomment the following line:
                // out.println(separatedSentences(lemmaOutput));
            }
        }
        scanner.close();
        out.close();

    }

    public static String[] seperatedSentences(String input) {
        // (\\.) or a question mark (\\?) but doesn't include the period
        // or question mark in the match. This allows the split to occur
        // after a period or question mark without consuming them.
        return input.split("(?<=[.?])\\s+");
        // \\s+ matches one or more whitespace characters
        // (spaces, tabs, newlines) immediately after the period or question mark.
    }

    // Takes a string as an input
    // Return the same string but lemmatized
    public static String Lemma(String input) {

        CoreDocument coreDocument = new CoreDocument(input);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();

        String[] words = new String[coreLabelList.size()];

        int i = 0;
        for (CoreLabel coreLabel : coreLabelList) {
            words[i] = coreLabel.lemma();
            i++;

        }
        return String.join(" ", words);
    }

    public static String POS(String lemma_output) {

        CoreDocument coreDocument = new CoreDocument(lemma_output);

        stanfordCoreNLP.annotate(coreDocument);

        List<CoreLabel> coreLabelList = coreDocument.tokens();

        String[] words = new String[coreLabelList.size()];

        int i = 0;
        for (CoreLabel coreLabel : coreLabelList) {

            words[i] = coreLabel.get(CoreAnnotations.PartOfSpeechAnnotation.class);
            i++;

        }
        return String.join(" ", words);
    }

    public static String PatternCheck(String POSoutput) {
        String[] words = POSoutput.split("\\s+");

        boolean foundDT = false;
        boolean foundNN = false;
        boolean foundVBP = false;
        boolean foundNNP = false;
        //boolean foundJJ = false;

        // Pattern 1: DT NN VBP NN
        for (String word : words) {
            if (!foundDT && word.equals("DT")) {
                foundDT = true;
            } else if (foundDT && !foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundDT && foundNN && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundDT && foundNN && foundVBP && word.equals("NN")) {
                return "Pattern found: DT NN VBP NN";
            }
        }

        // Pattern 2: NNP VBP NN
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNNP && foundVBP && word.equals("NN")) {
                return "Pattern found: NNP VBP NN";
            }
        }

        // Pattern 3: NN VBP NN
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNN && foundVBP && word.equals("NN")) {
                return "Pattern found: NN VBP NN";
            }
        }

        // Pattern 4: DT NN VBP JJ
        for (String word : words) {
            if (!foundDT && word.equals("DT")) {
                foundDT = true;
            } else if (foundDT && !foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundDT && foundNN && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundDT && foundNN && foundVBP && word.equals("JJ")) {
                return "Pattern found: DT NN VBP JJ";
            }
        }

        // Pattern 5: NNP VBP JJ
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNNP && foundVBP && word.equals("JJ")) {
                return "Pattern found: NNP VBP JJ";
            }
        }

        // Pattern 6: NN VBP JJ
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNN && foundVBP && word.equals("JJ")) {
                return "Pattern found: NN VBP JJ";
            }
        }

        return "Pattern not found";
    }
}
