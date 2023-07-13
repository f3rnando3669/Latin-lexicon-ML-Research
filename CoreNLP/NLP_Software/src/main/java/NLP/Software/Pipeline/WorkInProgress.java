package NLP.Software.Pipeline;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

public class WorkInProgress {

    // Create a static instance of StanfordCoreNLP pipeline
    public static StanfordCoreNLP stanfordCoreNLP = Pipeline.getPipeline();

    // Main method
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
                // Declare a variable to store the formatted HashMap contents exclusive to each sentence
                StringBuilder HashMapOutput = new StringBuilder();

                StringBuilder IndexMapOutput = new StringBuilder();

                // Lemmatize the sentence
                String lemmaOutput = Lemma(sentence);

                // Perform Part-of-Speech tagging on the lemmatized sentence
                String posOutput = POS(lemmaOutput);

                Map<Integer, String> indexmap = IndexPoSConnect(posOutput);

                // Check for specific patterns in the Part-of-Speech tags
                String patternMatchedOutput = PatternCheck(posOutput, indexmap);

                // Convert the pattern string to an array
                String[] patternArray = PatternToArray(patternMatchedOutput);

                // Connect lemmas and POS tags into a map
                Map<String, String> wordMap = ConnectLemmaPOS(lemmaOutput, posOutput);

                // Find matched words based on the patterns and word map
                String wordMatch = MatchedWords(patternArray, wordMap);

                // Append each key-value pair from the word map to HashMapOutput
                for (Map.Entry<String, String> entry : wordMap.entrySet()) {
                    HashMapOutput.append(entry.getKey()).append(" -> ").append(entry.getValue()).append("\n");
                }

                for (Map.Entry<Integer, String> entry : indexmap.entrySet()) {
                    IndexMapOutput.append(entry.getKey()).append(" -> ").append(entry.getValue()).append("\n");
                }

                // Write the results to the output file
                out.println("Input: " + sentence + "\nPost-Lemma: " + lemmaOutput + "\nPost-POS: " + posOutput + "\nPattern Matching: " + patternMatchedOutput + "\nIndexMapOutput\n" + IndexMapOutput + "\nConnect Output:\n" + HashMapOutput + "Matched Words: " + wordMatch + "\n");

                // If you want to write the separated sentences to a file, uncomment the following line:
                // out.println(separatedSentences(lemmaOutput));
            }
        }
        scanner.close();
        out.close();
    }

    // Separate input into sentences
    public static String[] seperatedSentences(String input) {
        // (\\.) or a question mark (\\?) but doesn't include the period
        // or question mark in the match. This allows the split to occur
        // after a period or question mark without consuming them.
        return input.split("(?<=[.?])\\s+");
        // \\s+ matches one or more whitespace characters
        // (spaces, tabs, newlines) immediately after the period or question mark.
    }

    // Lemmatize the input string
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

    // Perform Part-of-Speech tagging on the input string
    public static String POS(String lemmaOutput) {
        CoreDocument coreDocument = new CoreDocument(lemmaOutput);
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

    public static Map<Integer, String> IndexPoSConnect(String posOutput) {
        String[] posWords = splitIntoWords(posOutput);

        Map<Integer, String> indexmap = new LinkedHashMap<>();

        for (int i = 0; i < posWords.length; i++) {
            String value = posWords[i];

            indexmap.put(i, value);
        }

        return indexmap;
    }

    // Check for specific patterns in the Part-of-Speech tags
    public static String PatternCheck(String POSoutput, Map<Integer, String> indexMap) {
        String[] words = POSoutput.split("\\s+");
        // Key is number/Index
        // Value is posOutput
        int index = 0;
        boolean foundDT = false;
        boolean foundNN = false;
        boolean foundNN1 = false;
        boolean foundVBP = false;
        boolean foundVB = false;
        boolean foundNNP = false;
        boolean foundJJ = false;

        // Pattern 1: DT NN VBP NN
        for (String word : words) {
            for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
                if (entry.getValue().equals("DT") && word.equals(entry.getValue())) {
                    foundDT = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1: Found DT");
                    System.out.println(entry.getValue());
                    System.out.println(index);

                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundNN = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1: Found NN");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("VBP") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundVBP = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1: Found VBP");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    index = entry.getKey();
                    System.out.println("Pattern 1: Found NN again");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                    foundNN1 = true;
                }
                if (foundDT && foundNN && foundVBP && foundNN1) {
                    return "DT NN VBP NN";
                }
            }
        }

        index = 0;
        foundDT = false;
        foundNN = false;
        foundNN1 = false;
        foundVBP = false;
        foundVB = false;
        foundNNP = false;
        foundJJ = false;

        // Pattern 1.2: DT NN VB NN
        for (String word : words) {
            for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
                if (entry.getValue().equals("DT") && word.equals(entry.getValue())) {
                    foundDT = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1.2: Found DT");
                    System.out.println(entry.getValue());
                    System.out.println(index);

                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundNN = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1.2: Found NN");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("VB") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundVB = true;
                    index = entry.getKey();
                    System.out.println("Pattern 1.2: Found VB");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    index = entry.getKey();
                    System.out.println("Pattern 1.2: Found NN again");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                    foundNN1 = true;
                }
                if (foundDT && foundNN && foundVB && foundNN1) {
                    return "DT NN VB NN";
                }
            }
        }

        index = 0;
        foundDT = false;
        foundNN = false;
        foundNN1 = false;
        foundVBP = false;
        foundVB = false;
        foundNNP = false;
        foundJJ = false;

        // Pattern 4.2: DT NN VB JJ
        for (String word : words) {
            for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
                if (entry.getValue().equals("DT") && word.equals(entry.getValue())) {
                    foundDT = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found DT");
                    System.out.println(entry.getValue());
                    System.out.println(index);

                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundNN = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found NN");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("VB") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundVB = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found VBP");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("JJ") && word.equals(entry.getValue())) {
                    if (entry.getKey() > index) {
                        foundJJ = true;
                        index = entry.getKey();
                        System.out.println("Pattern 4.2: Found JJ");
                        System.out.println(entry.getValue());
                        System.out.println(index);
                    } else return "No";
                }
                if (foundDT && foundNN && foundVB && foundJJ) {
                    return "DT NN VB JJ";
                }
            }
        }

        // Pattern 2: NNP VBP NN
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNNP && foundVBP && word.equals("NN")) {
                return "NNP VBP NN";
            }
        }

        // Pattern 2.2: NNP VB NN
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVB && word.equals("VB")) {
                foundVB = true;
            } else if (foundNNP && foundVB && word.equals("NN")) {
                return "NNP VB NN";
            }
        }

        // Pattern 3: NN VBP NN
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVBP && word.equals("VBP")) {
                foundVBP = true;
            } else if (foundNN && foundVBP && word.equals("NN")) {
                return "NN VBP NN";
            }
        }

        // Pattern 3.2: NN VB NN
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVB && word.equals("VB")) {
                foundVB = true;
            } else if (foundNN && foundVB && word.equals("NN")) {
                return "NN VB NN";
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
                return "DT NN VBP JJ";
            }
        }

        // Pattern 4.2: DT NN VB JJ
        for (String word : words) {
            for (Map.Entry<Integer, String> entry : indexMap.entrySet()) {
                if (entry.getValue().equals("DT") && word.equals(entry.getValue())) {
                    foundDT = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found DT");
                    System.out.println(entry.getValue());
                    System.out.println(index);

                }
                if (entry.getValue().equals("NN") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundNN = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found NN");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("VB") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundVB = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found VBP");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (entry.getValue().equals("JJ") && word.equals(entry.getValue()) && entry.getKey() > index) {
                    foundJJ = true;
                    index = entry.getKey();
                    System.out.println("Pattern 4.2: Found JJ");
                    System.out.println(entry.getValue());
                    System.out.println(index);
                }
                if (foundDT && foundNN && foundVB && foundJJ) {
                    return "DT NN VB JJ";
                }
            }
        }

        // Pattern 5: NNP VBP JJ
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVB && word.equals("VBP")) {
                foundVB = true;
            } else if (foundNNP && foundVB && word.equals("JJ")) {
                return "NNP VBP JJ";
            }
        }

        // Pattern 5.2: NNP VBP JJ
        for (String word : words) {
            if (!foundNNP && word.equals("NNP")) {
                foundNNP = true;
            } else if (foundNNP && !foundVBP && word.equals("VB")) {
                foundVBP = true;
            } else if (foundNNP && foundVBP && word.equals("JJ")) {
                return "NNP VB JJ";
            }
        }

        // Pattern 6:NN VBP JJ
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVB && word.equals("VBP")) {
                foundVB = true;
            } else if (foundNN && foundVB && word.equals("JJ")) {
                return "NN VBP JJ";
            }
        }

        // Pattern 6.2:NN VBP JJ
        for (String word : words) {
            if (!foundNN && word.equals("NN")) {
                foundNN = true;
            } else if (foundNN && !foundVB && word.equals("VB")) {
                foundVB = true;
            } else if (foundNN && foundVB && word.equals("JJ")) {
                return "NN VB JJ";
            }
        }

        return "Pattern not found";
    }

    // Split a sentence into individual words
    public static String[] splitIntoWords(String sentence) {
        return sentence.split("\\s+");
    }

    // Connect lemmas and POS tags into a map
    public static Map<String, String> ConnectLemmaPOS(String lemmaInput, String posOutput) {
        String[] lemmaWords = splitIntoWords(lemmaInput);
        String[] posWords = splitIntoWords(posOutput);

        // Create a LinkedHashMap to store the mapping of lemmaWords to posWords
        Map<String, String> wordMap = new LinkedHashMap<>();

        // Iterate over the arrays and put the elements into the LinkedHashMap
        for (int i = 0; i < lemmaWords.length; i++) {
            String lemma = lemmaWords[i];
            String pos = i + ". " + posWords[i];

            // Generate a unique key for each word by appending its index
            String key = i + ". " + lemma;

            // Put the word and its corresponding POS tag into the map
            wordMap.put(pos, key);
        }

        // Returning the LinkedHashMap
        return wordMap;
    }

    // Convert pattern string to an array of words
    public static String[] PatternToArray(String patternOutput) {
        return splitIntoWords(patternOutput);
    }

    // Find matched words based on patterns and word map
    public static String MatchedWords(String[] pattern, Map<String, String> wordMap) {
        StringBuilder matchedWords = new StringBuilder();

        // Iterate over the pattern array
        for (String patternWord : pattern) {
            // Iterate over the wordMap entries
            for (Map.Entry<String, String> entry : wordMap.entrySet()) {
                if (entry.getValue().equals(patternWord)) {
                    // Append the matching key to the matchedWords StringBuilder
                    matchedWords.append(entry.getKey()).append(" ");

                    break; // Break the inner loop to move to the next pattern word
                }
            }
        }

        return matchedWords.toString().trim(); // Trim any trailing whitespace and return the result
    }
}
