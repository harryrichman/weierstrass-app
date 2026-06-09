/* Find the Weierstrass locus of a graph, with attached multiplicities */

function weierstrassLocus(graph) {
    // pass
}


// Compute reduced divisors

function reducedDiv(id) {
    adj = buildEdgeList();
    $.ajax({
        method: "POST",
        url: "get-reduced-div",
        data: {
            adj: adj,     // list of edges
            base_v: id,   // index of base point
        },
        dataType: "json",
        success: function(json) {
            updateGraph(json, id);
        }
    });
}

function canonicalDiv(graph) {
    // graph is an Object with nodes and links attributes
    var degrees = {};
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
        const node = graph.nodes[i];
        node["canonical_div"] = degrees[node["id"]] - 2;
    }
}


// Utility

function buildEdgeList() {
    // cy is the global Cytoscape instance defined in index.html
    const edges = cy.edges().map(e => [
        parseInt(e.data('source')),
        parseInt(e.data('target')),
    ]);
    const edgeString = JSON.stringify(edges);
    $('#edgejson').text(edgeString);
    return edgeString;
}

function updateGraph(json, q_id) {
    const n_nodes = cy.nodes().length;
    for (const id in json) {
        const m = json[id];
        const idx = parseInt(id);
        const node = cy.$id(String(idx));
        if (node.length === 0) {
            // node not found, skip
        } else {
            node.data('label', String(m));
            if (idx == q_id) {
                if (m > n_nodes / 2) {
                    node.style({ 'background-color': 'red',    'border-color': 'DarkGray' });
                } else {
                    node.style({ 'background-color': 'yellow', 'border-color': 'DarkGray' });
                }
            } else if (m > 0) {
                node.style({ 'background-color': 'yellow' });
            }
        }
    }
}

function defaultColors() {
    cy.nodes().forEach(function(node) {
        node.style({ 'background-color': 'LightGray', 'border-color': 'DarkGray' });
        node.data('label', '0');
    });
}


$(document).ready(function() {
    cy.on('tap', 'node', function(evt) {
        const id = parseInt(evt.target.id());
        console.log("tap node:", id);
        defaultColors();
        reducedDiv(id);
    });
});