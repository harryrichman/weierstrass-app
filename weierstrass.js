/* Find the Weierstrass locus of a graph, with attached multiplicities */

function weierstrassLocus(graph) {
    // pass
}


// Compute reduced divisors

function canonicalDiv(graph) {
    // graph is an Object with nodes and links attributes
    var degrees = {}
    for (i = 0; i < graph.nodes.length; i++) {
        const id = graph.nodes[i].id;
        degrees[id] = 0;
    }
    for (j = 0; j < graph.links.length; j++) {
        const edge = graph.links[j];
        const s = edge.source.id;
        const t = edge.target.id;
        degrees[s] += 1;
        degrees[t] += 1;
    }
    for (i = 0; i < graph.nodes.length; i++) {
        // const id = graph.nodes[i]["id"];
        // graph.nodes[i]["canonical_div"] = degrees[id] - 2;
        const node = graph.nodes[i];
        node["canonical_div"] = degrees[node["id"]] - 2;
    }
}