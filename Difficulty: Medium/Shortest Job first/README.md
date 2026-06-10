<h2><a href="https://www.geeksforgeeks.org/problems/shortest-job-first/1">Shortest Job first</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next. </span><span style="font-size: 18px;">Given an array of integers <strong>bt[]</strong> of size <strong>n</strong>. Array <strong>bt[]</strong> denotes the <strong>burst time</strong> of each process. Calculate the <strong>average waiting time</strong> of all the processes and return the&nbsp;nearest integer which is smaller or equal to the output.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> Consider all process are available at time 0.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>bt[] = [4,3,7,1,2]
<strong>Output: </strong>4
<strong>Explanation:</strong> After sorting burst times by shortest job policy, calculated average waiting time is 4.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>bt[] = [1,2,3,4]
<strong>Output: </strong>2
<strong>Explanation:</strong> After sorting burst times by shortest job policy, calculated average waiting time is 2.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= n &lt;= 10<sup>5</sup></span><br><span style="font-size: 18px;">1 &lt;= arr[i] &lt;= 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Greedy</code>&nbsp;