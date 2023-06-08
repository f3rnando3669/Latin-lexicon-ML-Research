package main.nlp;

import java.io.*;
import java.util.*;

import edu.stanford.nlp.ling.*;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.util.*;
import edu.stanford.nlp.semgraph.*;

public class ConstituencyParseExample {

    public static void main (String[] args) throws IOException {

        // set up properties
        Properties props = new Properties();
        props.setProperty("ssplit.eolonly","true");
        props.setProperty("annotators",
                "tokenize, ssplit, pos, parse");
        // set up pipeline
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
        // get contents from file
        
             Annotation annotation =
                new Annotation("A dog is an animal.");
        // annotate
         pipeline.annotate(annotation);
        // get tree
        Tree tree =
                annotation.get(CoreAnnotations.SentencesAnnotation.class).get(0).get(TreeCoreAnnotations.TreeAnnotation.class);
        System.out.println(tree);
        Set<Constituent> treeConstituents = tree.constituents(new LabeledScoredConstituentFactory());
        for (Constituent constituent : treeConstituents) {
            if (constituent.label() != null &&
                    (constituent.label().toString().equals("VP") || constituent.label().toString().equals("NP"))) {
                System.err.println("found constituent: "+constituent.toString());
                System.err.println(tree.getLeaves().subList(constituent.start(), constituent.end()+1));
            }
        }


    }

}
