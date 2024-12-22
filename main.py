from collections import defaultdict
import time
import sys


# Prepare the list of fragments
def create_fragments_list(source_file):
    f = open(source_file, "r")
    return list(map(lambda x: x.strip(), f.readlines()))


# Find the longest path using DFS
def dfs_longest_path(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start) # Mark the current node as visited
    path.append(start)

    longest_path = list(path)  # Keep track of the longest path found so far

    for neighbor in graph[start]:
        if neighbor not in visited:
            current_path = dfs_longest_path(graph, neighbor, visited, path)
            if len(current_path) > len(longest_path):
                longest_path = current_path

    path.pop()  # Backtrack: remove the current node from the path
    visited.remove(start)  # Backtrack: unmark the current node as visited

    return longest_path


class Puzzle:
    def __init__(self, source_file):
        self.fragments_list = create_fragments_list(source_file)
        self.graph = self.create_graph()

    def create_graph(self):
        graph = defaultdict(list)

        for num_str in self.fragments_list:
            right_part = num_str[-2:]
            for other in self.fragments_list:
                left_part = other[:2]
                if right_part == left_part and num_str != other:
                    graph[num_str].append(other)
        return graph


    def find_longest_sequence(self):
        longest_seq = []
        print("Searching for longest sequence...")
        for num_str in self.fragments_list:
            sys.stdout.write(". ")
            sys.stdout.flush()
            time.sleep(0.1)

            current_longest = dfs_longest_path(self.graph, num_str)
            if len(current_longest) > len(longest_seq):
                longest_seq = current_longest
                sys.stdout.write(f"\rNew longest path found, with length: {len(longest_seq)}")
                sys.stdout.flush()
        print("\nSearch complete.")
        print("======")
        print(f"The longest sequence is {len(longest_seq)} fragments long.")
        print("Resulting puzzle:", ''.join(longest_seq))
        return longest_seq


if __name__ == '__main__':
    puzzle = Puzzle('source.txt')
    puzzle.find_longest_sequence()