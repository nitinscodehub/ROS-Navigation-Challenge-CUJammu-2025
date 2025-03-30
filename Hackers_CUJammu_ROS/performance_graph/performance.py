import matplotlib.pyplot as plt


maze_levels = ['Easy', 'Medium', 'Hard']
steps_attempt1 = [50, 68, 85]
steps_attempt2 = [45, 62, 78]


plt.figure(figsize=(10,6))
plt.plot(maze_levels, steps_attempt1, 'b-o', label='Attempt 1', linewidth=2)
plt.plot(maze_levels, steps_attempt2, 'r--s', label='Attempt 2', linewidth=2)
plt.title('Steps vs Maze Difficulty', fontsize=14, fontweight='bold')
plt.xlabel('Maze Complexity', fontsize=12)
plt.ylabel('Steps Taken', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('performance_graph.png', dpi=300, bbox_inches='tight')