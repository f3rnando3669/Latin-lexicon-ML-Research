package main.nlp;

import java.io.*;
import java.util.*;

import edu.stanford.nlp.ling.*;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.util.*;
import edu.stanford.nlp.semgraph.*;

public class DependencyTreeExample {

    public static void main (String[] args) throws IOException {

        // set up properties
        Properties props = new Properties();
        props.setProperty("ssplit.eolonly","true");
        props.setProperty("annotators",
                "tokenize, ssplit, pos, parse");
        // set up pipeline
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
        // get contents from file
        
        String content =  "A dog is an animal.";//new Scanner(new File(args[0])).useDelimiter("\\Z").next();
        System.out.println(content);
        // read in a product review per line
        Annotation annotation = new Annotation(content);
        pipeline.annotate(annotation);

        List<CoreMap> sentences = annotation.get(CoreAnnotations.SentencesAnnotation.class);
        for (CoreMap sentence : sentences) {
            System.out.println("---");
            System.out.println("sentence: "+sentence);
            SemanticGraph tree = sentence.get(SemanticGraphCoreAnnotations.CollapsedCCProcessedDependenciesAnnotation.class);
            System.out.println(tree.toString(SemanticGraph.OutputFormat.READABLE));
        }
}
