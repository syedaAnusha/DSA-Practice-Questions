<h2><a href="https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1">Shortest Distance in a Binary Maze</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given a binary matrix <strong>mat[][]</strong> of size <strong>n × m</strong> containing values 0 and 1, and a source cell <strong>src[]</strong> and destination cell <strong>dest[]</strong>, find the minimum number of steps required to reach the destination cell from the source cell. From any cell, you can move to its adjacent cells in the up, down, left, and right directions.</span></p>
<ul>
<li><span style="font-size: 14pt;">1 represents a traversable cell.</span></li>
<li><span style="font-size: 14pt;">0 represents a blocked cell that cannot be visited.</span></li>
</ul>
<p><span style="font-size: 14pt;">If the destination cannot be reached from the source, return -1.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:</span></strong><span style="font-size: 18px;"> <span style="font-size: 14pt;">mat</span>[][] = {{1, 1, 1, 1},{1, 1, 0, 1},{1, 1, 1, 1},{1, 1, 0, 0},{1, 0, 0, 1}}</span><span style="font-size: 18px;">, </span><span style="font-size: 18px;">src[] = {0, 1}</span><span style="font-size: 18px;">, </span><span style="font-size: 18px;">dest[] = {2, 2}</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Output:</span> </strong></span><span style="font-size: 18px;">3</span>
<span style="font-size: 18px;"><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;">From (0,1), the minimum number of steps to reach (2,2) is 3.</span><strong style="font-size: 18px;"><br></strong></span><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/929635/Web/Other/blobid0_1781266963.png" width="300" height="165"> &nbsp;</pre>
<pre><strong><span style="font-size: 18px;">Input:</span><span style="font-size: 14pt;"> </span></strong><span style="font-size: 14pt;">mat</span><span style="font-size: 18px;">[][] = {{1, 1, 1, 1, 1},{1, 1, 1, 1, 1},{1, 1, 1, 1, 0},{1, 0, 1, 0, 1}}</span><span style="font-size: 18px;">, </span><span style="font-size: 18px;">src[] = {0, 0}</span><span style="font-size: 18px;">, </span><span style="font-size: 18px;">dest[] = {3, 4}</span>
<span style="font-size: 18px;"><strong>Output:</strong></span><span style="font-size: 18px;">-1</span>
<span style="font-size: 18px;"><strong>Explanation:</strong></span><span style="font-size: 18px;">From (0,0), the destination (3,4) cannot be reached because all possible paths are blocked by 0 cells, so no valid route exists.</span>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/929635/Web/Other/blobid1_1781266978.png" width="343" height="158"> </pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">1 ≤ n, m ≤ 500</span></li>
<li><span style="font-size: 18px;">grid[i][j] == 0 or grid[i][j] == 1</span></li>
<li><span style="font-size: 18px;">The source and destination cells are always inside the given matrix.</span></li>
</ul></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Samsung</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Matrix</code>&nbsp;<code>Graph</code>&nbsp;<code>BFS</code>&nbsp;