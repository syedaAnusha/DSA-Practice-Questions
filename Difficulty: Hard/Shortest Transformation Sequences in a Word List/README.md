<h2><a href="https://www.geeksforgeeks.org/problems/word-ladder-ii/1">Shortest Transformation Sequences in a Word List</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given two distinct words <strong>s</strong>&nbsp;and <strong>e</strong>, and a list of unique words <strong>words[]</strong>, where all words have the same length, find all <strong>shortest</strong> transformation <strong>sequences</strong> from s to e.</span></p>
<p><span style="font-size: 18px;">A valid transformation sequence must satisfy the following conditions:</span></p>
<ul>
<li><span style="font-size: 18px;">Only <strong>one</strong> character can be changed in each transformation.</span></li>
<li><span style="font-size: 18px;">Every transformed word must <strong>exist</strong> in words[], including e.</span></li>
<li><span style="font-size: 18px;">All words consist only of lowercase English letters.</span></li>
<li><span style="font-size: 18px;"><strong>s</strong> may or may not be present in words[].</span></li>
</ul>
<p><span style="font-size: 18px;">Return all shortest transformation sequences from s to e. If no such sequence exists, return an <strong>empty</strong> list. The sequences may be returned in any order.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">s = "der", e = "dfs", words[] = ["des", "der", "dfr", "dgt", "dfs"]
<strong>Output: </strong>[["der", "des", "dfs"], ["der", "dfr", "dfs"]]
<strong>Explanation: </strong></span><span style="font-size: 18px;">There are two shortest transformation sequences from "der" to "dfs", each having a length of 3:
"der" -&gt; "d<strong>f</strong>r" -&gt; "df<strong>s</strong>"
"der" -&gt; "de<strong>s</strong>" -&gt; "d<strong>f</strong>s"
Each transformation changes exactly one character, and every intermediate word belongs to words[]. Since these are the shortest possible sequences, both are included in the output.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "gedk", e = "geek", words[] = ["geek", "gefk"]
<strong>Output: </strong>[["gedk", "geek"]]<br><strong>Explanation:</strong> The word "gedk" can be transformed directly into "geek" by changing the third character ['d' to 'e']. Since "geek" is present in words[], the shortest transformation sequence is:
"gedk" -&gt; "ge<strong>e</strong>k"
Therefore, the output contains a single sequence.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 500, where n is the length of words.<br>1 ≤ m ≤ 10, where m is the length of words[i]<br>The sum of all shortest sequences does not exceed<span style="font-size: 14pt;"> 10<sup>5</sup>.&nbsp;<sup><br><span style="font-size: 14pt;">Let k is the number of shortest transformation sequences.</span></sup></span></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Adobe</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Graph</code>&nbsp;<code>BFS</code>&nbsp;