1.) By using a python program I coded, I found that the two real numbers x were:
-17.509122 and 11.68736. 
I found -17.509122 using the bracket {-20, -15}, and 11.68736 with {10, 15}. 
The determinant error using -17.509122 as x is .048308, (determinant was 4999.951692)
and using 11.68736 as x is .013596. (determinant was 5000.013596)

X-Values:	      -17.509122	   11.68736
Determinant:	 4999.951692	   5000.013596
Error:	           .048308	   .013596

Matrix = ([
[1,2,3,x],
[4,5,x,6],
[7,x,8,9],
[x,10,11,12]
])


2.)	The equation x^2 – 2 = 0 can be composed as the following three functions in terms of G:
-	G(x) = 2/x
-	G(x) = x^2 + x – 2
-	G(x) = (x+2)/(x+1)
The original equation x^2 – 2 = 0 has a root of sqrt(2). The only G function that converges is G(x) = (x+2)/(x+1), which converges to 1.4142 (approx. sqrt(2)).
The other 2 G functions diverge because when evaluating their G’(sqrt(2)), the absolute value of that answer is not less than 1.

G(x):	                    2/x        x^2 + x -2      (x+2)/(x+1)
G’(x):	                  -2/x^2	   2x+1	           -1/(x+1)^2
G’(sqrt(2)):	            -1	       3.828	         -0.1716
-1 < G’(sqrt(2)) < 1:	    No	       No	             Yes


4.) After analytically and graphically proving that there is only one positive root in the interval (0,1) of the function f(x) = ln^2(x) - x - 1, I used a python program that utilizes Newton's Method to find the largest possible b, such that b <= 1, that converged to the positive root a. I found that b = 0.66, with a solution of a = 0.31735.
