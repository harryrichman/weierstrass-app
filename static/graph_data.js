// Helper: wrap a flat node object into Cytoscape element format
function cyNode(n) {
  return { data: { id: String(n.id), label: n.label || String(n.id), title: n.title } };
}

// Helper: wrap a flat edge object into Cytoscape element format
function cyEdge(e, idx) {
  return { data: { id: 'e' + idx, source: String(e.from), target: String(e.to) } };
}

function toCyNodes(nodes) { return nodes.map(cyNode); }
function toCyEdges(edges) { return edges.map(cyEdge); }

// ── Triangle prism ────────────────────────────────────────────────────────────
// (renamed from tri_prism_ to triangle_prism_ to match the dropdown value)
const triangle_prism_nodes = toCyNodes(
  Array.from({ length: 6 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const triangle_prism_edges = toCyEdges([
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 1 },
  { from: 1, to: 4 },
  { from: 2, to: 5 },
  { from: 3, to: 6 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 4 },
]);

// ── Frucht ────────────────────────────────────────────────────────────────────
const frucht_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const frucht_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 3,  to: 4  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 6,  to: 7  },
  { from: 7,  to: 1  },
  { from: 1,  to: 8  },
  { from: 2,  to: 8  },
  { from: 3,  to: 9  },
  { from: 4,  to: 9  },
  { from: 5,  to: 10 },
  { from: 6,  to: 10 },
  { from: 7,  to: 11 },
  { from: 8,  to: 11 },
  { from: 9,  to: 12 },
  { from: 10, to: 12 },
  { from: 11, to: 12 },
]);


const frucht_like_1_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i, title: `vertex ${i + 1}` }))
);
const frucht_like_1_edges = toCyEdges([
  {from: 0, to: 1},
  {from: 0, to: 6},
  {from: 0, to: 10},
  {from: 1, to: 2},
  {from: 1, to: 7},
  {from: 2, to: 3},
  {from: 2, to: 7},
  {from: 3, to: 4},
  {from: 3, to: 8},
  {from: 4, to: 5},
  {from: 4, to: 9},
  {from: 5, to: 6},
  {from: 5, to: 11},
  {from: 6, to: 11},
  {from: 7, to: 8},
  {from: 8, to: 9},
  {from: 9, to: 10},
  {from: 10, to: 11}
]);

const frucht_like_2_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i, title: `vertex ${i + 1}` }))
);
const frucht_like_2_edges = toCyEdges([
  {from: 0, to: 1},
  {from: 0, to: 2},
  {from: 0, to: 3},
  {from: 1, to: 10},
  {from: 1, to: 11},
  {from: 2, to: 9},
  {from: 2, to: 11},
  {from: 3, to: 8},
  {from: 3, to: 10},
  {from: 4, to: 5},
  {from: 4, to: 6},
  {from: 4, to: 10},
  {from: 5, to: 6},
  {from: 5, to: 7},
  {from: 6, to: 9},
  {from: 7, to: 8},
  {from: 7, to: 9},
  {from: 8, to: 11}
]);

const frucht_like_3_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i, title: `vertex ${i + 1}` }))
);
const frucht_like_3_edges = toCyEdges([
  {from: 0, to: 1},
  {from: 0, to: 6},
  {from: 0, to: 10},
  {from: 1, to: 2},
  {from: 1, to: 7},
  {from: 2, to: 3},
  {from: 2, to: 7},
  {from: 3, to: 4},
  {from: 3, to: 11},
  {from: 4, to: 5},
  {from: 4, to: 8},
  {from: 5, to: 6},
  {from: 5, to: 9},
  {from: 6, to: 11},
  {from: 7, to: 8},
  {from: 8, to: 9},
  {from: 9, to: 10},
  {from: 10, to: 11}
]);

const frucht_like_4_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i, title: `vertex ${i + 1}` }))
);
const frucht_like_4_edges = toCyEdges([
  {from: 0, to: 1},
  {from: 0, to: 6},
  {from: 0, to: 10},
  {from: 1, to: 2},
  {from: 1, to: 7},
  {from: 2, to: 3},
  {from: 2, to: 7},
  {from: 3, to: 4},
  {from: 3, to: 8},
  {from: 4, to: 5},
  {from: 4, to: 10},
  {from: 5, to: 6},
  {from: 5, to: 8},
  {from: 6, to: 9},
  {from: 7, to: 11},
  {from: 8, to: 9},
  {from: 9, to: 11},
  {from: 10, to: 11}
]);

// ── Franklin ──────────────────────────────────────────────────────────────────
const franklin_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const franklin_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 3,  to: 4  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 6,  to: 7  },
  { from: 7,  to: 8  },
  { from: 8,  to: 9  },
  { from: 9,  to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 1  },
  { from: 1,  to: 8  },
  { from: 2,  to: 7  },
  { from: 3,  to: 10 },
  { from: 4,  to: 9  },
  { from: 5,  to: 12 },
  { from: 6,  to: 11 },
]);

// Truncated tetrahedron
const trunc_tetrahedron_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const trunc_tetrahedron_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 1,  to: 3  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 4,  to: 6  },
  { from: 7,  to: 8  },
  { from: 8,  to: 9  },
  { from: 7,  to: 9 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 10, to: 12  },
  { from: 1,  to: 4  },
  { from: 2,  to: 7  },
  { from: 3,  to: 10 },
  { from: 5,  to: 8  },
  { from: 9,  to: 11 },
  { from: 6,  to: 12 },
]);

// ── Dürer ─────────────────────────────────────────────────────────────────────
const durer_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const durer_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 3,  to: 4  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 6,  to: 1  },
  { from: 7,  to: 9  },
  { from: 8,  to: 10 },
  { from: 9,  to: 11 },
  { from: 10, to: 12 },
  { from: 11, to: 7  },
  { from: 12, to: 8  },
  { from: 1,  to: 7  },
  { from: 2,  to: 8  },
  { from: 3,  to: 9  },
  { from: 4,  to: 10 },
  { from: 5,  to: 11 },
  { from: 6,  to: 12 },
]);

// ── Bidiakis cube ─────────────────────────────────────────────────────────────
const bidiakis_nodes = toCyNodes(
  Array.from({ length: 12 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const bidiakis_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 3,  to: 4  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 6,  to: 7  },
  { from: 7,  to: 8  },
  { from: 8,  to: 9  },
  { from: 9,  to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 1  },
  { from: 1,  to: 9  },
  { from: 2,  to: 8  },
  { from: 3,  to: 7  },
  { from: 4,  to: 12 },
  { from: 5,  to: 11 },
  { from: 6,  to: 10 },
]);

// ── Pappus ────────────────────────────────────────────────────────────────────
const pappus_nodes = toCyNodes(
  Array.from({ length: 18 }, (_, i) => ({ id: i + 1, title: `vertex ${i + 1}` }))
);
const pappus_edges = toCyEdges([
  { from: 1,  to: 2  },
  { from: 2,  to: 3  },
  { from: 3,  to: 4  },
  { from: 4,  to: 5  },
  { from: 5,  to: 6  },
  { from: 6,  to: 7  },
  { from: 7,  to: 8  },
  { from: 8,  to: 9  },
  { from: 9,  to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 13 },
  { from: 13, to: 14 },
  { from: 14, to: 15 },
  { from: 15, to: 16 },
  { from: 16, to: 17 },
  { from: 17, to: 18 },
  { from: 18, to: 1  },
  { from: 1,  to: 6  },
  { from: 2,  to: 9  },
  { from: 3,  to: 14 },
  { from: 4,  to: 11 },
  { from: 5,  to: 16 },
  { from: 7,  to: 12 },
  { from: 8,  to: 15 },
  { from: 10, to: 17 },
  { from: 13, to: 18 },
]);