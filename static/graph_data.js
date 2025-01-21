
const tri_prism_nodes = Array.from({ length: 6 }, (_, i) => i + 1).map(
  idx => ({ id: idx, title: `vertex ${idx}` })
);
const tri_prism_edges = [
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 1 },
  { from: 1, to: 4 },
  { from: 2, to: 5 },
  { from: 3, to: 6 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 4 },
];

const frucht_nodes = [
  { id: 1, label: "1", title: "vertex 1" },
  { id: 2, label: "2", title: "vertex 2" },
  { id: 3, label: "3", title: "vertex 3" },
  { id: 4, label: "4", title: "vertex 4" },
  { id: 5, label: "5", title: "vertex 5" },
  { id: 6, label: "6", title: "vertex 6" },
  { id: 7, label: "7", title: "vertex 7" },
  { id: 8, label: "8", title: "vertex 8" },
  { id: 9, label: "9", title: "vertex 9" },
  { id: 10, label: "10", title: "vertex 10" },
  { id: 11, label: "11", title: "vertex 11" },
  { id: 12, label: "12", title: "vertex 12" },
];
const frucht_edges = [
  { from: 1, to: 2, color: undefined },
  { from: 2, to: 3 },
  { from: 3, to: 4 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 7 },
  { from: 7, to: 1 },
  { from: 1, to: 8 },
  { from: 2, to: 8 },
  { from: 3, to: 9 },
  { from: 4, to: 9 },
  { from: 5, to: 10 },
  { from: 6, to: 10 },
  { from: 7, to: 11 },
  { from: 8, to: 11 },
  { from: 9, to: 12 },
  { from: 10, to: 12 },
  { from: 11, to: 12 },
];

const franklin_nodes = Array.from({ length: 12 }, (_, i) => i + 1).map(
  idx => ({ id: idx, title: `vertex ${idx}` })
);
const franklin_edges = [
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 4 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 7 },
  { from: 7, to: 8 },
  { from: 8, to: 9 },
  { from: 9, to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 1 },
  { from: 1, to: 8 },
  { from: 2, to: 7 },
  { from: 3, to: 10 },
  { from: 4, to: 9 },
  { from: 5, to: 12 },
  { from: 6, to: 11 },
];

const durer_nodes = Array.from({ length: 12 }, (_, i) => i + 1).map(
  idx => ({ id: idx, title: `vertex ${idx}` })
);
const durer_edges = [
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 4 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 1 },
  { from: 7, to: 9 },
  { from: 8, to: 10 },
  { from: 9, to: 11 },
  { from: 10, to: 12 },
  { from: 11, to: 7 },
  { from: 12, to: 8 },
  { from: 1, to: 7 },
  { from: 2, to: 8 },
  { from: 3, to: 9 },
  { from: 4, to: 10 },
  { from: 5, to: 11 },
  { from: 6, to: 12 },
];

const bidiakis_nodes = Array.from({ length: 12 }, (_, i) => i + 1).map(
  idx => ({ id: idx, title: `vertex ${idx}` })
);
const bidiakis_edges = [
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 4 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 7 },
  { from: 7, to: 8 },
  { from: 8, to: 9 },
  { from: 9, to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 1 },
  { from: 1, to: 9 },
  { from: 2, to: 8 },
  { from: 3, to: 7 },
  { from: 4, to: 12 },
  { from: 5, to: 11 },
  { from: 6, to: 10 },
];

const pappus_nodes = Array.from({ length: 18 }, (_, i) => i + 1).map(
  idx => ({ id: idx, title: `vertex ${idx}` })
);
const pappus_edges = [
  { from: 1, to: 2 },
  { from: 2, to: 3 },
  { from: 3, to: 4 },
  { from: 4, to: 5 },
  { from: 5, to: 6 },
  { from: 6, to: 7 },
  { from: 7, to: 8 },
  { from: 8, to: 9 },
  { from: 9, to: 10 },
  { from: 10, to: 11 },
  { from: 11, to: 12 },
  { from: 12, to: 13 },
  { from: 13, to: 14 },
  { from: 14, to: 15 },
  { from: 15, to: 16 },
  { from: 16, to: 17 },
  { from: 17, to: 18 },
  { from: 18, to: 1 },
  { from: 1, to: 6 },
  { from: 2, to: 9 },
  { from: 3, to: 14 },
  { from: 4, to: 11 },
  { from: 5, to: 16 },
  { from: 7, to: 12 },
  { from: 8, to: 15 },
  { from: 10, to: 17 },
  { from: 13, to: 18 },
];

