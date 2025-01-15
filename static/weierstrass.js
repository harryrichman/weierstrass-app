/* Find the Weierstrass locus of a graph, with attached multiplicities */

function weierstrassLocus(graph) {
    // pass
}


// Compute reduced divisors

function reducedDiv(id) {
    adj = buildEdgeList()
    // debugging
    console.log("adj: " + adj)
    $.ajax({
        method: "POST",
        url: "get-reduced-div",
        data: {
            adj: adj, // list of edges
            base_v: id, // index of base point
        },
        dataType: "json",
        success: function(json) {
            console.log(json);
            updateGraph(json, id);
        }
    })
}

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

// utility 


function buildEdgeList() {
    edges = Object.values(network.body.edges).map(x => [x.fromId, x.toId]);
    console.log("edges: ")
    console.log(edges)
    edgeString = JSON.stringify(edges);
    console.log("edgeString: " + edgeString)
    $('#edgejson').text(edgeString);
    return edgeString;
}

function updateGraph(json, q_id) {
    // debug
    console.log(frucht_nodes)
    for (const id in json) {
        const m = json[id];
        const idx = parseInt(id);
        console.log("type of m: " + typeof m)
        var node = frucht_nodes.get(idx);
        if (node === null) {
            // console.log("node " + id + " not found");
        }
        else {
            // console.log("node found: " + id)
            node.label = String(m);
            if (idx == q_id) {
                if (m > 6) {
                    node.color = {
                        border: "DarkGray",
                        background: "red",
                    };    
                } else {
                    node.color = {
                        border: "DarkGray",
                        background: "orange",
                    };    
                }
            } else if (m > 0) {
                node.color = {
                    background: "yellow",
                }
            }
            frucht_nodes.update(node);    
        }
    }
}

$(document).ready(function() {
    network.on("selectNode", function (params) {
        console.log("selectNode Event:", params);
        defaultColors();
        const id = params.nodes[0]
        colorNode(id);
        reducedDiv(id);
      });


})