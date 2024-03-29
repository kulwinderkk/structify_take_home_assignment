## Take Home Assignment Sturctify

# Actionables of the project:
1. **Solve the Question:** Given a list of chords in a circle, count the number of intersections, if any. For simplicity’s sake, assume all starting and ending points are unique.
    
    *Input:*
    *Two lists: one being an identifier of the chord and the other being the radian measure. The values themselves are radians and sorted in ascending order. Look below for more clarity.*

    *Input Example: For instance, in the below example, there is one intersection, and given the far right point of the circle is 0, the input might be something like* 

    *[(0.78, 1.47, 1.77, 3.92), (“s1”, “s2”, “e1”, “e2”)]*

    *Radian measurements=(0.78, 1.47, 1.77, 3.92)*
    *Identifiers=(“s1”, “s2”, “e1”, “e2”)*

2. **Coding:** Write an algorithm to count the number of intersections. Provide a README.md with steps to calculate it and how to run the file.

3. **Submission:** When you are done, make it a private GitHub repository and share it with “Reichenbachian” (our reviewer). Then, please submit this take-home assignment below by attaching a zip-file with your README and code. In the notes section below, please write your GitHub username.


# Assumptions:

1. **Since it was mentioned in the question that we are provided two lists, I have solved the problem assuming we have two input lists one for radian measurements and one for identifiers.**
-  Radian Measurements-> a list where radians are arranged in ascending order.
-  Identifiers-> a list with start and end for each chord mentioned as 's1', 'e1' with 's', and 'e' followed by the chord number respectively.

The input example that was provided with the question had one list with two tuples. I have ignored that and assumed our input as below:

*Input Example:* 

*[0.78, 1.47, 1.77, 3.92]*
*[“s1”, “s2”, “e1”, “e2”]*

*Radian measurements=[0.78, 1.47, 1.77, 3.92]*
*Identifiers=[“s1”, “s2”, “e1”, “e2”]*

2. The identifier is always supplied in the format mentioned in the example. It can be in any order. 
    Example -> ['s1', 's2', 'e1', 'e2']
3. The radian measurements are added in the ascending order.
4. No intersections will occur at the same point.
5. Only intersections that happen inside the circle count as intersections, as chords don’t continue outside of the circle.
6. All starting and ending points are unique. 

# Solution Explanation

First, I'm making pairs of chords with start and end radian values stored in a tuple:
[chord1, chord2, chord3, chord4,....]
[('s1', 'e1'), ('s2', 'e2'), ('s3', 'e3'), c('s4', 'e4'),....]

Second, I want to ensure that the starting radian is always smaller than the ending radian.
's1' < 'e1' and repeat it for all the chords. 

Third, I want to reorder the chords in such a way that all the starting radians are arranged in ascending order.
[('s1', 'e1'), ('s2', 'e2'), ('s3', 'e3'), c('s4', 'e4'),....]

's1' < 's2' < 's3' < 's4' <......
The above steps are performed in the function `get_chord_pair`.

Fourth, I will loop over the chords list. Pick one chord in one iteration and check its intersection with the other chords. Repeate the process for rest of the chords and keep updating the counter each time there is an intersection.

To check the intersection of two chords :
Chord1 = ('s1', 'e1') 
chord2 = ('s2', 'e2')

Logic - if all of the conditions are matched then there is an intersection
1. s1<s2
2. e1>s2 
3. e1<e2 

This step is performed in the function `count_intersections`. 
# Play around with notebook and Python script.

You can run the notebook and script in the base environment.

1. Notebook - Specify the radian_measures and identifiers each time you run the cell block.
You will get a visualization and number of intersection counts.

2. Script - run the script as 

`python count_chord_intersection.py`

Input the radian measures and Identifiers, it will return the number of intersections.

