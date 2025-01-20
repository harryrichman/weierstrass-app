/* Find the Weierstrass locus of a graph, with attached multiplicities */

function weierstrassLocus(graph) {
    // pass
}


// Compute reduced divisors

function reducedDiv(id) {
    adj = buildEdgeList()
    // debugging
    // console.log("adj: " + adj)
    $.ajax({
        method: "POST",
        url: "get-reduced-div",
        data: {
            adj: adj, // list of edges
            base_v: id, // index of base point
        },
        dataType: "json",
        success: function(json) {
            // console.log(json);
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
    // console.log("edges: ")
    // console.log(edges)
    edgeString = JSON.stringify(edges);
    // console.log("edgeString: " + edgeString)
    $('#edgejson').text(edgeString);
    return edgeString;
}

function updateGraph(json, q_id) {
    // debug
    // console.log(visjs_nodes)
    for (const id in json) {
        const m = json[id];
        const idx = parseInt(id);
        var node = visjs_nodes.get(idx);
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
            visjs_nodes.update(node);    
        }
    }
}

function defaultColors() {
    // console.log("running default colors fn")
    for (let i = 1; i <= visjs_nodes.length; i++) {
        var node = visjs_nodes.get(i);
        node.color = {
            border: "DarkGray",
            background: "LightGray",
        };
        node.label = "0";
        visjs_nodes.update(node);
    }
}

function handleSelectionChange() {
    // Get the selected value from the dropdown
    const dropdown = document.getElementById('graph-dropdown');
    // const selectedValue = dropdown.value;

    // Display the selected value in the output paragraph
    const output = document.getElementById('output');
    output.textContent = `You selected: ${dropdown.options[dropdown.selectedIndex].text}`;

    if (dropdown.value) {
        visjs_nodes.clear();
        visjs_edges.clear();

    }
    if (dropdown.value == "triangle-prism") {
        visjs_nodes.add(tri_prism_nodes);
        visjs_edges.add(tri_prism_edges);
    } else if (dropdown.value == "frucht") {
        visjs_nodes.add(frucht_nodes);
        visjs_edges.add(frucht_edges);
    } else if (dropdown.value == "pappus") {
        visjs_nodes.add(pappus_nodes);
        visjs_edges.add(pappus_edges);
    } else if (dropdown.value == "franklin") {
        visjs_nodes.add(franklin_nodes);
        visjs_edges.add(franklin_edges);
    } else if (dropdown.value == "durer") {
        visjs_nodes.add(durer_nodes);
        visjs_edges.add(durer_edges);
    } else if (dropdown.value == "bidiakis") {
        visjs_nodes.add(bidiakis_nodes);
        visjs_edges.add(bidiakis_edges);
    }
}

// function colorNode(id) {
//     var selected_node = visjs_nodes.get(id)
//     selected_node.color = {
//       border: "red",
//       background: "red",
//     }
//     selected_node.label = "1",
//     visjs_nodes.update(selected_node)
// }

  $(document).ready(function() {
    network.on("selectNode", function (params) {
        console.log("selectNode Event:", params);
        defaultColors();
        const id = params.nodes[0]
        // colorNode(id);
        reducedDiv(id);
      });


})