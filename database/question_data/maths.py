# 100 High-Quality Conceptual & Numerical Mathematics MCQs

MATHS_QUESTIONS = [
    # 1 - 10: Algebra, Complex Numbers & Quadratic Equations
    {
        "question_text": "If alpha and beta are the roots of the quadratic equation x^2 - 6x + 8 = 0, what is the value of (alpha^2 + beta^2)?",
        "option_a": "20",
        "option_b": "36",
        "option_c": "52",
        "option_d": "16",
        "correct_option": "A",
        "explanation": "alpha + beta = 6, alpha * beta = 8. alpha^2 + beta^2 = (alpha + beta)^2 - 2 alpha beta = (6)^2 - 2(8) = 36 - 16 = 20.",
        "difficulty": "High"
    },
    {
        "question_text": "For what value of k will the quadratic equation 4x^2 - 12x + k = 0 have real and equal roots?",
        "option_a": "k = 9",
        "option_b": "k = 36",
        "option_c": "k = 3",
        "option_d": "k = 12",
        "correct_option": "A",
        "explanation": "For equal roots, discriminant D = b^2 - 4ac = 0 => (-12)^2 - 4(4)(k) = 0 => 144 - 16k = 0 => 16k = 144 => k = 9.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the modulus and principal argument of the complex number z = 1 + i sqrt(3)?",
        "option_a": "|z| = 2, Arg(z) = pi / 3",
        "option_b": "|z| = 4, Arg(z) = pi / 6",
        "option_c": "|z| = 2, Arg(z) = pi / 6",
        "option_d": "|z| = sqrt(2), Arg(z) = pi / 3",
        "correct_option": "A",
        "explanation": "|z| = sqrt(1^2 + (sqrt(3))^2) = sqrt(1 + 3) = 2. Arg(z) = tan^-1(sqrt(3) / 1) = pi / 3 (60 degrees).",
        "difficulty": "High"
    },
    {
        "question_text": "If omega is a complex cube root of unity, what is the value of (1 - omega + omega^2) * (1 + omega - omega^2)?",
        "option_a": "4",
        "option_b": "2",
        "option_c": "1",
        "option_d": "0",
        "correct_option": "A",
        "explanation": "1 + omega + omega^2 = 0 => 1 + omega^2 = -omega and 1 + omega = -omega^2. Expression = (-omega - omega) * (-omega^2 - omega^2) = (-2 omega) * (-2 omega^2) = 4 omega^3 = 4(1) = 4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the sum of the infinite geometric progression (GP): 1/2 + 1/4 + 1/8 + 1/16 + ...?",
        "option_a": "1",
        "option_b": "2",
        "option_c": "1/2",
        "option_d": "3/2",
        "correct_option": "A",
        "explanation": "Sum of infinite GP = a / (1 - r). First term a = 1/2, common ratio r = 1/2. S_infinity = (1/2) / (1 - 1/2) = (1/2) / (1/2) = 1.",
        "difficulty": "High"
    },
    {
        "question_text": "If the 5th term of an Arithmetic Progression (AP) is 19 and the 11th term is 43, what is the first term 'a' and common difference 'd'?",
        "option_a": "a = 3, d = 4",
        "option_b": "a = 5, d = 3",
        "option_c": "a = 1, d = 4",
        "option_d": "a = 3, d = 5",
        "correct_option": "A",
        "explanation": "a + 4d = 19, a + 10d = 43. Subtracting equations: 6d = 24 => d = 4. Then a = 19 - 4(4) = 19 - 16 = 3.",
        "difficulty": "High"
    },
    {
        "question_text": "How many 4-digit numbers can be formed using the digits 1, 2, 3, 4, 5, 6 without repetition?",
        "option_a": "360",
        "option_b": "720",
        "option_c": "120",
        "option_d": "24",
        "correct_option": "A",
        "explanation": "Number of permutations P(6, 4) = 6! / (6 - 4)! = 6 * 5 * 4 * 3 = 360.",
        "difficulty": "High"
    },
    {
        "question_text": "In how many ways can a committee of 5 people be chosen from 7 men and 4 women such that the committee contains exactly 3 men and 2 women?",
        "option_a": "210",
        "option_b": "462",
        "option_c": "105",
        "option_d": "35",
        "correct_option": "A",
        "explanation": "Ways = C(7, 3) * C(4, 2) = [(7 * 6 * 5) / (3 * 2 * 1)] * [(4 * 3) / (2 * 1)] = 35 * 6 = 210.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the coefficient of x^3 in the expansion of (1 + 2x)^5?",
        "option_a": "80",
        "option_b": "40",
        "option_c": "160",
        "option_d": "10",
        "correct_option": "A",
        "explanation": "General term T_(r+1) = C(5, r) * 1^(5-r) * (2x)^r. For x^3, r = 3. Coefficient = C(5, 3) * 2^3 = 10 * 8 = 80.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the middle term in the expansion of (x + 2/x)^8?",
        "option_a": "1120",
        "option_b": "70",
        "option_c": "448",
        "option_d": "280",
        "correct_option": "A",
        "explanation": "n = 8 (even), so middle term is (8/2 + 1) = 5th term (r = 4). T5 = C(8, 4) * (x)^4 * (2/x)^4 = 70 * x^4 * (16 / x^4) = 70 * 16 = 1120.",
        "difficulty": "High"
    },

    # 11 - 20: Matrices, Determinants & Trigonometry
    {
        "question_text": "If matrix A = [[2, 3], [1, 4]], what is the determinant |A| and inverse matrix A^-1?",
        "option_a": "|A| = 5, A^-1 = (1/5) [[4, -3], [-1, 2]]",
        "option_b": "|A| = 11, A^-1 = (1/11) [[4, -3], [-1, 2]]",
        "option_c": "|A| = 5, A^-1 = (1/5) [[2, -1], [-3, 4]]",
        "option_d": "|A| = 10, A^-1 = [[4, 3], [1, 2]]",
        "correct_option": "A",
        "explanation": "|A| = (2*4) - (3*1) = 8 - 3 = 5. Adj(A) = [[4, -3], [-1, 2]]. A^-1 = (1/|A|) Adj(A) = (1/5) [[4, -3], [-1, 2]].",
        "difficulty": "High"
    },
    {
        "question_text": "If A is a 3x3 square matrix such that determinant |A| = 4, what is the value of |det(2A)|?",
        "option_a": "32",
        "option_b": "8",
        "option_c": "24",
        "option_d": "16",
        "correct_option": "A",
        "explanation": "For an n x n matrix A, det(k A) = k^n * det(A). Here n = 3, k = 2 => det(2A) = 2^3 * det(A) = 8 * 4 = 32.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of sin(15 degrees)?",
        "option_a": "(sqrt(6) - sqrt(2)) / 4",
        "option_b": "(sqrt(6) + sqrt(2)) / 4",
        "option_c": "(sqrt(3) - 1) / 2",
        "option_d": "(sqrt(3) + 1) / (2 sqrt(2))",
        "correct_option": "A",
        "explanation": "sin(15) = sin(45 - 30) = sin(45)cos(30) - cos(45)sin(30) = (1/sqrt(2))(sqrt(3)/2) - (1/sqrt(2))(1/2) = (sqrt(3) - 1) / (2 sqrt(2)) = (sqrt(6) - sqrt(2)) / 4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the principal value of tan^-1(1) + cos^-1(-1/2) + sin^-1(-1/2)?",
        "option_a": "3 pi / 4",
        "option_b": "pi / 4",
        "option_c": "5 pi / 4",
        "option_d": "pi / 2",
        "correct_option": "A",
        "explanation": "tan^-1(1) = pi/4. cos^-1(-1/2) = 2pi/3. sin^-1(-1/2) = -pi/6. Total = pi/4 + 2pi/3 - pi/6 = pi/4 + 4pi/6 - pi/6 = pi/4 + 3pi/6 = pi/4 + pi/2 = 3pi/4.",
        "difficulty": "High"
    },
    {
        "question_text": "If tan(A) = 1/2 and tan(B) = 1/3, what is the value of (A + B)?",
        "option_a": "pi / 4 (45 degrees)",
        "option_b": "pi / 6 (30 degrees)",
        "option_c": "pi / 3 (60 degrees)",
        "option_d": "pi / 2 (90 degrees)",
        "correct_option": "A",
        "explanation": "tan(A + B) = [tan(A) + tan(B)] / [1 - tan(A)tan(B)] = (1/2 + 1/3) / [1 - (1/2)(1/3)] = (5/6) / (5/6) = 1 => A + B = pi / 4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the general solution of the trigonometric equation sin(x) = 1/2?",
        "option_a": "x = n pi + (-1)^n * (pi / 6), where n in Z",
        "option_b": "x = 2 n pi +/- (pi / 6), where n in Z",
        "option_c": "x = n pi +/- (pi / 3), where n in Z",
        "option_d": "x = n pi + (pi / 6), where n in Z",
        "correct_option": "A",
        "explanation": "For sin(x) = sin(alpha) with alpha = pi/6, general solution is x = n pi + (-1)^n * alpha.",
        "difficulty": "High"
    },
    {
        "question_text": "In triangle ABC with side lengths a = 5, b = 6, c = 7, what is the value of cos(A)?",
        "option_a": "5 / 7",
        "option_b": "19 / 35",
        "option_c": "3 / 5",
        "option_d": "12 / 35",
        "correct_option": "A",
        "explanation": "By law of cosines: cos(A) = (b^2 + c^2 - a^2) / (2 b c) = (36 + 49 - 25) / (2 * 6 * 7) = 60 / 84 = 5 / 7.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the domain of the function f(x) = sin^-1(2x - 1)?",
        "option_a": "[0, 1]",
        "option_b": "[-1, 1]",
        "option_c": "[0, 2]",
        "option_d": "[-1/2, 1/2]",
        "correct_option": "A",
        "explanation": "-1 <= 2x - 1 <= 1 => 0 <= 2x <= 2 => 0 <= x <= 1. Domain is [0, 1].",
        "difficulty": "High"
    },
    {
        "question_text": "If log_2(x) + log_2(x - 2) = 3, what is the value of x?",
        "option_a": "x = 4",
        "option_b": "x = 2",
        "option_c": "x = 8",
        "option_d": "x = -2",
        "correct_option": "A",
        "explanation": "log_2[x(x - 2)] = 3 => x(x - 2) = 2^3 = 8 => x^2 - 2x - 8 = 0 => (x - 4)(x + 2) = 0. Since x > 2 for logs to be defined, x = 4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the maximum and minimum value of the expression 3 sin(x) + 4 cos(x)?",
        "option_a": "Max = +5, Min = -5",
        "option_b": "Max = +7, Min = -7",
        "option_c": "Max = +12, Min = -12",
        "option_d": "Max = +1, Min = -1",
        "correct_option": "A",
        "explanation": "The expression a sin(x) + b cos(x) ranges between -sqrt(a^2 + b^2) and +sqrt(a^2 + b^2). Here sqrt(3^2 + 4^2) = sqrt(25) = 5.",
        "difficulty": "High"
    },

    # 21 - 30: Coordinate Geometry & 3D Vectors
    {
        "question_text": "What is the distance between the parallel lines 3x - 4y + 7 = 0 and 3x - 4y - 3 = 0?",
        "option_a": "2 units",
        "option_b": "4 units",
        "option_c": "10 units",
        "option_d": "1 unit",
        "correct_option": "A",
        "explanation": "Distance d = |c1 - c2| / sqrt(a^2 + b^2) = |7 - (-3)| / sqrt(3^2 + (-4)^2) = 10 / sqrt(25) = 10 / 5 = 2 units.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the center and radius of the circle given by x^2 + y^2 - 6x + 8y - 11 = 0?",
        "option_a": "Center (3, -4), Radius = 6",
        "option_b": "Center (-3, 4), Radius = 36",
        "option_c": "Center (6, -8), Radius = 11",
        "option_d": "Center (3, 4), Radius = 5",
        "correct_option": "A",
        "explanation": "g = -3, f = 4, c = -11. Center = (-g, -f) = (3, -4). Radius r = sqrt(g^2 + f^2 - c) = sqrt(9 + 16 - (-11)) = sqrt(36) = 6.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the equation of the parabola with focus at (2, 0) and directrix x = -2?",
        "option_a": "y^2 = 8x",
        "option_b": "x^2 = 8y",
        "option_c": "y^2 = 4x",
        "option_d": "y^2 = -8x",
        "correct_option": "A",
        "explanation": "Standard parabola y^2 = 4ax with a = 2 gives y^2 = 4(2)x = 8x.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the eccentricity 'e' of the ellipse x^2/25 + y^2/9 = 1?",
        "option_a": "e = 4 / 5 = 0.8",
        "option_b": "e = 3 / 5 = 0.6",
        "option_c": "e = 16 / 25",
        "option_d": "e = 5 / 4",
        "correct_option": "A",
        "explanation": "a^2 = 25, b^2 = 9. b^2 = a^2 (1 - e^2) => 9 = 25 (1 - e^2) => 1 - e^2 = 9/25 => e^2 = 16/25 => e = 4/5.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the scalar product (dot product) of vectors A = 3i - 2j + 4k and B = 2i + j - 3k?",
        "option_a": "-8",
        "option_b": "16",
        "option_c": "4",
        "option_d": "-2",
        "correct_option": "A",
        "explanation": "A . B = (3)(2) + (-2)(1) + (4)(-3) = 6 - 2 - 12 = -8.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the area of a parallelogram whose adjacent sides are represented by vectors A = i - j + 3k and B = 2i - 7j + k?",
        "option_a": "15 sqrt(2) sq units",
        "option_b": "30 sq units",
        "option_c": "15 sq units",
        "option_d": "450 sq units",
        "correct_option": "A",
        "explanation": "Cross product A x B = i(-1 + 21) - j(1 - 6) + k(-7 + 2) = 20i + 5j - 5k. Area = |A x B| = sqrt(20^2 + 5^2 + (-5)^2) = sqrt(400 + 25 + 25) = sqrt(450) = 15 sqrt(2) sq units.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the angle between the planes 2x - y + z = 6 and x + y + 2z = 3?",
        "option_a": "pi / 3 (60 degrees)",
        "option_b": "pi / 4 (45 degrees)",
        "option_c": "pi / 6 (30 degrees)",
        "option_d": "pi / 2 (90 degrees)",
        "correct_option": "A",
        "explanation": "Normal vectors n1 = (2, -1, 1), n2 = (1, 1, 2). cos(theta) = |n1 . n2| / (|n1||n2|) = |2 - 1 + 2| / (sqrt(4+1+1) * sqrt(1+1+4)) = 3 / (sqrt(6)*sqrt(6)) = 3 / 6 = 1/2 => theta = pi / 3.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the perpendicular distance of the point (1, 2, 3) from the plane 2x + 3y - 6z + 5 = 0?",
        "option_a": "5 / 7 units",
        "option_b": "13 / 7 units",
        "option_c": "1 / 7 units",
        "option_d": "3 units",
        "correct_option": "A",
        "explanation": "d = |2(1) + 3(2) - 6(3) + 5| / sqrt(2^2 + 3^2 + (-6)^2) = |2 + 6 - 18 + 5| / sqrt(4 + 9 + 36) = |-5| / sqrt(49) = 5 / 7 units.",
        "difficulty": "High"
    },
    {
        "question_text": "If vectors A = 2i - j + k, B = i + 2j - 3k, and C = 3i + lambda j + 5k are coplanar, what is the value of lambda?",
        "option_a": "-4",
        "option_b": "4",
        "option_c": "2",
        "option_d": "-2",
        "correct_option": "A",
        "explanation": "For coplanar vectors, scalar triple product det[[2, -1, 1], [1, 2, -3], [3, lambda, 5]] = 0. 2(10 + 3 lambda) + 1(5 + 9) + 1(lambda - 6) = 0 => 20 + 6 lambda + 14 + lambda - 6 = 0 => 7 lambda + 28 = 0 => 7 lambda = -28 => lambda = -4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the equation of the line passing through point (2, -1, 4) parallel to the vector 3i + 5j - 2k?",
        "option_a": "(x - 2)/3 = (y + 1)/5 = (z - 4)/(-2)",
        "option_b": "(x + 2)/3 = (y - 1)/5 = (z + 4)/(-2)",
        "option_c": "(x - 3)/2 = (y - 5)/(-1) = (z + 2)/4",
        "option_d": "3x + 5y - 2z = 0",
        "correct_option": "A",
        "explanation": "Cartesian line equation: (x - x1)/a = (y - y1)/b = (z - z1)/c => (x - 2)/3 = (y + 1)/5 = (z - 4)/(-2).",
        "difficulty": "High"
    },

    # 31 - 40: Calculus — Limits, Continuity & Differentiation
    {
        "question_text": "Evaluate the limit: lim_(x -> 0) [sin(5x) / x].",
        "option_a": "5",
        "option_b": "1",
        "option_c": "0",
        "option_d": "1/5",
        "correct_option": "A",
        "explanation": "lim_(x -> 0) [5 * (sin(5x) / (5x))] = 5 * 1 = 5.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the limit: lim_(x -> 0) [(1 - cos(2x)) / x^2].",
        "option_a": "2",
        "option_b": "1",
        "option_c": "4",
        "option_d": "1/2",
        "correct_option": "A",
        "explanation": "Using L'Hopital's rule twice: lim 2 sin(2x) / 2x = lim 4 cos(2x) / 2 = 4 / 2 = 2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the derivative of y = ln(sec(x) + tan(x)) with respect to x?",
        "option_a": "sec(x)",
        "option_b": "tan(x)",
        "option_c": "sec^2(x)",
        "option_d": "1 / (sec(x) + tan(x))",
        "correct_option": "A",
        "explanation": "dy/dx = (1 / (sec x + tan x)) * (sec x tan x + sec^2 x) = [sec x (tan x + sec x)] / (sec x + tan x) = sec(x).",
        "difficulty": "High"
    },
    {
        "question_text": "If x = a cos^3(theta) and y = a sin^3(theta), what is dy/dx at theta = pi/4?",
        "option_a": "-1",
        "option_b": "+1",
        "option_c": "0",
        "option_d": "sqrt(2)",
        "correct_option": "A",
        "explanation": "dx/d theta = -3a cos^2(theta) sin(theta). dy/d theta = 3a sin^2(theta) cos(theta). dy/dx = (dy/d theta) / (dx/d theta) = -tan(theta). At theta = pi/4, dy/dx = -tan(pi/4) = -1.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the derivative of y = x^x with respect to x?",
        "option_a": "x^x * (1 + ln(x))",
        "option_b": "x * x^(x-1)",
        "option_c": "x^x * ln(x)",
        "option_d": "x^x / (1 + ln(x))",
        "correct_option": "A",
        "explanation": "ln(y) = x ln(x) => (1/y) dy/dx = 1 * ln(x) + x(1/x) = 1 + ln(x) => dy/dx = x^x (1 + ln(x)).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the slope of the tangent to the curve y = 3x^2 - 4x + 1 at the point x = 2?",
        "option_a": "8",
        "option_b": "12",
        "option_c": "5",
        "option_d": "4",
        "correct_option": "A",
        "explanation": "dy/dx = 6x - 4. At x = 2, slope m = 6(2) - 4 = 12 - 4 = 8.",
        "difficulty": "High"
    },
    {
        "question_text": "At what point on the curve y = x^2 does the tangent make an angle of 45 degrees with the positive x-axis?",
        "option_a": "(1/2, 1/4)",
        "option_b": "(1, 1)",
        "option_c": "(2, 4)",
        "option_d": "(1/4, 1/16)",
        "correct_option": "A",
        "explanation": "Slope dy/dx = 2x = tan(45) = 1 => 2x = 1 => x = 1/2. Then y = (1/2)^2 = 1/4. Point is (1/2, 1/4).",
        "difficulty": "High"
    },
    {
        "question_text": "Find the maximum value of the function f(x) = -x^2 + 4x + 5 on R.",
        "option_a": "9",
        "option_b": "5",
        "option_c": "4",
        "option_d": "13",
        "correct_option": "A",
        "explanation": "f'(x) = -2x + 4 = 0 => x = 2. f''(x) = -2 < 0 (max at x = 2). f(2) = -(2)^2 + 4(2) + 5 = -4 + 8 + 5 = 9.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of c guaranteed by Rolle's Theorem for f(x) = x^2 - 4x + 3 on the interval [1, 3]?",
        "option_a": "c = 2",
        "option_b": "c = 1.5",
        "option_c": "c = 2.5",
        "option_d": "c = 0",
        "correct_option": "A",
        "explanation": "f(1) = 0, f(3) = 0. f'(c) = 2c - 4 = 0 => c = 2, which lies strictly inside (1, 3).",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the limit: lim_(x -> infinity) [(3x^2 + 5x - 2) / (2x^2 - 4x + 7)].",
        "option_a": "3 / 2",
        "option_b": "5 / 4",
        "option_c": "0",
        "option_d": "infinity",
        "correct_option": "A",
        "explanation": "Divide numerator and denominator by x^2: lim (3 + 5/x - 2/x^2) / (2 - 4/x + 7/x^2) = 3 / 2.",
        "difficulty": "High"
    },

    # 41 - 50: Integration & Definite Integrals
    {
        "question_text": "Evaluate the indefinite integral: integral (3x^2 + 4x - 5) dx.",
        "option_a": "x^3 + 2x^2 - 5x + C",
        "option_b": "3x^3 + 4x^2 - 5x + C",
        "option_c": "x^3 + 4x^2 - 5 + C",
        "option_d": "6x + 4 + C",
        "correct_option": "A",
        "explanation": "integral 3x^2 dx = x^3, integral 4x dx = 2x^2, integral -5 dx = -5x. Total = x^3 + 2x^2 - 5x + C.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the integral: integral (1 / (x^2 + 9)) dx.",
        "option_a": "(1/3) tan^-1(x / 3) + C",
        "option_b": "tan^-1(x / 3) + C",
        "option_c": "(1/9) tan^-1(x) + C",
        "option_d": "ln(x^2 + 9) + C",
        "correct_option": "A",
        "explanation": "Standard formula integral (1 / (x^2 + a^2)) dx = (1/a) tan^-1(x/a) + C. Here a = 3.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the definite integral: integral from 0 to pi/2 of sin^2(x) dx.",
        "option_a": "pi / 4",
        "option_b": "pi / 2",
        "option_c": "1",
        "option_d": "pi / 8",
        "correct_option": "A",
        "explanation": "sin^2(x) = (1 - cos(2x))/2. Integral = [x/2 - sin(2x)/4] from 0 to pi/2 = (pi/4 - 0) - (0 - 0) = pi / 4.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the integral using integration by parts: integral x * e^x dx.",
        "option_a": "e^x (x - 1) + C",
        "option_b": "e^x (x + 1) + C",
        "option_c": "x^2 * e^x / 2 + C",
        "option_d": "x * e^x + C",
        "correct_option": "A",
        "explanation": "u = x, dv = e^x dx => du = dx, v = e^x. Integral = x e^x - integral e^x dx = x e^x - e^x + C = e^x (x - 1) + C.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the definite integral: integral from 1 to e of (1 / x) dx.",
        "option_a": "1",
        "option_b": "e",
        "option_c": "0",
        "option_d": "e - 1",
        "correct_option": "A",
        "explanation": "[ln|x|] from 1 to e = ln(e) - ln(1) = 1 - 0 = 1.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the area enclosed between the parabola y = x^2 and the line y = 4?",
        "option_a": "32 / 3 sq units",
        "option_b": "16 / 3 sq units",
        "option_c": "8 / 3 sq units",
        "option_d": "64 / 3 sq units",
        "correct_option": "A",
        "explanation": "Points of intersection x = -2 to 2. Area = integral from -2 to 2 of (4 - x^2) dx = 2 * [4x - x^3/3] from 0 to 2 = 2 * [8 - 8/3] = 2 * (16/3) = 32 / 3 sq units.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the order and degree of the differential equation (d^2 y / dx^2)^3 + (dy / dx)^4 + y = 0?",
        "option_a": "Order = 2, Degree = 3",
        "option_b": "Order = 2, Degree = 4",
        "option_c": "Order = 3, Degree = 2",
        "option_d": "Order = 1, Degree = 4",
        "correct_option": "A",
        "explanation": "Highest order derivative present is d^2y/dx^2 (Order 2). The power of this highest derivative term is 3 (Degree 3).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the integrating factor (I.F.) for the linear differential equation dy/dx + (2 / x) y = x^2?",
        "option_a": "x^2",
        "option_b": "x",
        "option_c": "e^(2x)",
        "option_d": "ln(x^2)",
        "correct_option": "A",
        "explanation": "P(x) = 2 / x. I.F. = e^(integral P dx) = e^(integral (2/x) dx) = e^(2 ln x) = e^(ln x^2) = x^2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the general solution of the separable differential equation dy/dx = y / x?",
        "option_a": "y = c x",
        "option_b": "y = x + c",
        "option_c": "y^2 = x^2 + c",
        "option_d": "y = c / x",
        "correct_option": "A",
        "explanation": "dy / y = dx / x => ln|y| = ln|x| + ln|c| => ln|y| = ln|c x| => y = c x.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the integral: integral from -pi to pi of sin^5(x) dx.",
        "option_a": "0",
        "option_b": "2 pi",
        "option_c": "pi",
        "option_d": "4 / 5",
        "correct_option": "A",
        "explanation": "f(x) = sin^5(x) is an odd function (f(-x) = -f(x)). The integral of any odd function over symmetric limits [-a, a] is zero.",
        "difficulty": "High"
    },

    # 51 - 60: Probability & Statistics
    {
        "question_text": "Two fair dice are thrown simultaneously. What is the probability that the sum of the numbers appearing on top faces is equal to 8?",
        "option_a": "5 / 36",
        "option_b": "1 / 6",
        "option_c": "7 / 36",
        "option_d": "1 / 9",
        "correct_option": "A",
        "explanation": "Favorable outcomes for sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) -> 5 outcomes out of total 36. Probability = 5 / 36.",
        "difficulty": "High"
    },
    {
        "question_text": "If P(A) = 0.6, P(B) = 0.5, and P(A cap B) = 0.3, what is the conditional probability P(A | B)?",
        "option_a": "0.6",
        "option_b": "0.5",
        "option_c": "0.3",
        "option_d": "0.8",
        "correct_option": "A",
        "explanation": "P(A | B) = P(A cap B) / P(B) = 0.3 / 0.5 = 3 / 5 = 0.6.",
        "difficulty": "High"
    },
    {
        "question_text": "A bag contains 5 red balls and 3 black balls. Two balls are drawn at random one after another without replacement. What is the probability that both drawn balls are red?",
        "option_a": "5 / 14",
        "option_b": "25 / 64",
        "option_c": "15 / 56",
        "option_d": "5 / 8",
        "correct_option": "A",
        "explanation": "P(R1) = 5/8. P(R2 | R1) = 4/7. P(Both Red) = (5/8) * (4/7) = 20 / 56 = 5 / 14.",
        "difficulty": "High"
    },
    {
        "question_text": "If X is a binomially distributed random variable with n = 6 trials and probability of success p = 1/2, what is the variance of X?",
        "option_a": "1.5",
        "option_b": "3.0",
        "option_c": "0.75",
        "option_d": "2.25",
        "correct_option": "A",
        "explanation": "Mean = n p = 6 * (1/2) = 3. Variance = n * p * q = 6 * (1/2) * (1/2) = 6 / 4 = 1.5.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the mean and variance of the first 5 natural numbers (1, 2, 3, 4, 5)?",
        "option_a": "Mean = 3, Variance = 2",
        "option_b": "Mean = 3, Variance = 2.5",
        "option_c": "Mean = 2.5, Variance = 2",
        "option_d": "Mean = 3, Variance = 4",
        "correct_option": "A",
        "explanation": "Mean = (1+2+3+4+5)/5 = 15/5 = 3. Variance = (n^2 - 1)/12 for first n natural numbers = (25 - 1)/12 = 24/12 = 2.",
        "difficulty": "High"
    },
    {
        "question_text": "If events A and B are independent such that P(A) = 0.4 and P(B) = 0.5, what is P(A cup B)?",
        "option_a": "0.7",
        "option_b": "0.9",
        "option_c": "0.2",
        "option_d": "0.6",
        "correct_option": "A",
        "explanation": "Since A and B are independent, P(A cap B) = P(A) * P(B) = 0.4 * 0.5 = 0.2. P(A cup B) = P(A) + P(B) - P(A cap B) = 0.4 + 0.5 - 0.2 = 0.7.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the number of terms in the expansion of (x + y + z)^10?",
        "option_a": "66",
        "option_b": "11",
        "option_c": "55",
        "option_d": "100",
        "correct_option": "A",
        "explanation": "Number of terms in multinomial expansion (x1 + x2 + ... + xk)^n is C(n + k - 1, k - 1). Here n = 10, k = 3 => C(10 + 3 - 1, 3 - 1) = C(12, 2) = (12 * 11) / 2 = 66.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the arithmetic mean of the roots of the cubic polynomial x^3 - 9x^2 + 26x - 24 = 0?",
        "option_a": "3",
        "option_b": "9",
        "option_c": "8",
        "option_d": "2",
        "correct_option": "A",
        "explanation": "Sum of roots = -(-9)/1 = 9. Since there are 3 roots, Arithmetic Mean = 9 / 3 = 3.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of 1/(1*2) + 1/(2*3) + 1/(3*4) + ... + 1/(n*(n+1))?",
        "option_a": "n / (n + 1)",
        "option_b": "1 / (n + 1)",
        "option_c": "(n + 1) / n",
        "option_d": "n^2 / (n + 1)",
        "correct_option": "A",
        "explanation": "T_k = 1/[k(k+1)] = 1/k - 1/(k+1). Telescoping sum = (1 - 1/2) + (1/2 - 1/3) + ... + (1/n - 1/(n+1)) = 1 - 1/(n+1) = n / (n + 1).",
        "difficulty": "High"
    },
    {
        "question_text": "If a matrix A is symmetric as well as skew-symmetric, then A must be:",
        "option_a": "A zero matrix",
        "option_b": "A unit matrix",
        "option_c": "A diagonal matrix",
        "option_d": "A scalar matrix",
        "correct_option": "A",
        "explanation": "A = A^T (symmetric) and A = -A^T (skew-symmetric) => A = -A => 2A = 0 => A is a zero matrix.",
        "difficulty": "High"
    },

    # 61 - 70: Trigonometry, Coordinate Geometry & Vectors
    {
        "question_text": "What is the slope of the line perpendicular to 4x - 3y + 12 = 0?",
        "option_a": "-3 / 4",
        "option_b": "4 / 3",
        "option_c": "3 / 4",
        "option_d": "-4 / 3",
        "correct_option": "A",
        "explanation": "Slope of 4x - 3y + 12 = 0 is m1 = 4/3. Perpendicular slope m2 = -1 / m1 = -3 / 4.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the length of the latus rectum of the hyperbola x^2/16 - y^2/9 = 1?",
        "option_a": "9 / 2 = 4.5 units",
        "option_b": "9 units",
        "option_c": "8 units",
        "option_d": "32 / 3 units",
        "correct_option": "A",
        "explanation": "a^2 = 16 => a = 4; b^2 = 9. Length of latus rectum = 2 b^2 / a = 2(9) / 4 = 18 / 4 = 9 / 2 = 4.5 units.",
        "difficulty": "High"
    },
    {
        "question_text": "Find the locus of a point which moves such that its distance from point (3, 0) is equal to its distance from y-axis.",
        "option_a": "y^2 - 6x + 9 = 0",
        "option_b": "x^2 - 6y + 9 = 0",
        "option_c": "y^2 + 6x - 9 = 0",
        "option_d": "x^2 + y^2 = 9",
        "correct_option": "A",
        "explanation": "Distance to (3,0): sqrt((x-3)^2 + y^2). Distance to y-axis: |x|. Equating: (x-3)^2 + y^2 = x^2 => x^2 - 6x + 9 + y^2 = x^2 => y^2 - 6x + 9 = 0.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the angle between the vectors A = i + j and B = j + k?",
        "option_a": "pi / 3 (60 degrees)",
        "option_b": "pi / 4 (45 degrees)",
        "option_c": "pi / 2 (90 degrees)",
        "option_d": "2 pi / 3 (120 degrees)",
        "correct_option": "A",
        "explanation": "A . B = (1)(0) + (1)(1) + (0)(1) = 1. |A| = sqrt(2), |B| = sqrt(2). cos(theta) = 1 / (sqrt(2)*sqrt(2)) = 1/2 => theta = pi / 3.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the projection of vector A = 2i + 3j + 2k on the vector B = i + 2j + k?",
        "option_a": "10 / sqrt(6)",
        "option_b": "10 / sqrt(17)",
        "option_c": "5 / sqrt(6)",
        "option_d": "8 / sqrt(6)",
        "correct_option": "A",
        "explanation": "Projection = (A . B) / |B|. A . B = 2(1) + 3(2) + 2(1) = 2 + 6 + 2 = 10. |B| = sqrt(1^2 + 2^2 + 1^2) = sqrt(6). Projection = 10 / sqrt(6).",
        "difficulty": "High"
    },
    {
        "question_text": "If line (x - 1)/2 = (y - 2)/3 = (z - 3)/4 lies in the plane ax + by + cz = d, what is the value of 2a + 3b + 4c?",
        "option_a": "0",
        "option_b": "1",
        "option_c": "9",
        "option_d": "24",
        "correct_option": "A",
        "explanation": "The direction vector of the line (2, 3, 4) must be perpendicular to the plane normal vector (a, b, c). Therefore, 2a + 3b + 4c = 0.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the maximum value of sin(x) * cos(x)?",
        "option_a": "1 / 2",
        "option_b": "1",
        "option_c": "1 / 4",
        "option_d": "1 / sqrt(2)",
        "correct_option": "A",
        "explanation": "sin(x) cos(x) = (1/2) sin(2x). Maximum value occurs when sin(2x) = 1, giving 1/2.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of cos(20 deg) * cos(40 deg) * cos(80 deg)?",
        "option_a": "1 / 8",
        "option_b": "1 / 4",
        "option_c": "1 / 16",
        "option_d": "sqrt(3) / 8",
        "correct_option": "A",
        "explanation": "Standard identity: cos(A) cos(2A) cos(4A) = sin(8A) / (8 sin A). For A = 20 deg, sin(160)/(8 sin 20) = sin(20)/(8 sin 20) = 1 / 8.",
        "difficulty": "High"
    },
    {
        "question_text": "If tan^-1(x) + tan^-1(y) = pi / 4, what relation holds between x and y?",
        "option_a": "x + y + xy = 1",
        "option_b": "x + y - xy = 1",
        "option_c": "x + y = 1",
        "option_d": "x y = 1",
        "correct_option": "A",
        "explanation": "tan^-1[(x + y) / (1 - xy)] = pi / 4 => (x + y) / (1 - xy) = tan(pi / 4) = 1 => x + y = 1 - xy => x + y + xy = 1.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the range of the function f(x) = x / (1 + x^2) for x in R?",
        "option_a": "[-1/2, 1/2]",
        "option_b": "[-1, 1]",
        "option_c": "[0, 1/2]",
        "option_d": "(-infinity, infinity)",
        "correct_option": "A",
        "explanation": "Let y = x / (1 + x^2) => y x^2 - x + y = 0. For real x, D = 1 - 4 y^2 >= 0 => 4 y^2 <= 1 => -1/2 <= y <= 1/2.",
        "difficulty": "High"
    },

    # 71 - 80: Differential Equations & Definite Integrals
    {
        "question_text": "What is the solution of the differential equation dy/dx + y = e^(-x)?",
        "option_a": "y = (x + c) e^(-x)",
        "option_b": "y = c e^(-x)",
        "option_c": "y = e^x + c",
        "option_d": "y = (x^2 / 2 + c) e^(-x)",
        "correct_option": "A",
        "explanation": "I.F. = e^(integral 1 dx) = e^x. y e^x = integral e^x e^(-x) dx = integral 1 dx = x + c => y = (x + c) e^(-x).",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the definite integral: integral from 0 to 1 of x * (1 - x)^9 dx.",
        "option_a": "1 / 110",
        "option_b": "1 / 90",
        "option_c": "1 / 100",
        "option_d": "1 / 120",
        "correct_option": "A",
        "explanation": "By property integral from 0 to a of f(x) dx = integral from 0 to a of f(a - x) dx: Integral = integral from 0 to 1 of (1 - x) x^9 dx = [x^10 / 10 - x^11 / 11] from 0 to 1 = 1/10 - 1/11 = 1 / 110.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the integral: integral (x * cos(x)) dx.",
        "option_a": "x sin(x) + cos(x) + C",
        "option_b": "x sin(x) - cos(x) + C",
        "option_c": "x cos(x) + sin(x) + C",
        "option_d": "-x sin(x) + cos(x) + C",
        "correct_option": "A",
        "explanation": "Integration by parts: u = x, dv = cos(x) dx => du = dx, v = sin(x). Integral = x sin(x) - integral sin(x) dx = x sin(x) + cos(x) + C.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the area of the region bounded by the curve y = sin(x) between x = 0 and x = pi?",
        "option_a": "2 sq units",
        "option_b": "1 sq unit",
        "option_c": "pi sq units",
        "option_d": "4 sq units",
        "correct_option": "A",
        "explanation": "Area = integral from 0 to pi of sin(x) dx = [-cos(x)] from 0 to pi = -cos(pi) - (-cos(0)) = 1 + 1 = 2 sq units.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the differential equation of all circles passing through the origin with centers on x-axis?",
        "option_a": "x^2 - y^2 + 2xy (dy/dx) = 0",
        "option_b": "x^2 + y^2 + 2xy (dy/dx) = 0",
        "option_c": "y^2 - x^2 + 2xy (dy/dx) = 0",
        "option_d": "x (dy/dx) + y = 0",
        "correct_option": "A",
        "explanation": "Circle equation (x - g)^2 + y^2 = g^2 => x^2 - 2gx + y^2 = 0 => 2g = (x^2 + y^2)/x. Differentiating gives x^2 - y^2 + 2xy (dy/dx) = 0.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the limit: lim_(x -> 0) [(e^x - 1 - x) / x^2].",
        "option_a": "1 / 2",
        "option_b": "1",
        "option_c": "0",
        "option_d": "1 / 6",
        "correct_option": "A",
        "explanation": "Using Taylor series e^x = 1 + x + x^2/2! + ... => (e^x - 1 - x) / x^2 = 1/2! + x/3! + ... Taking limit as x -> 0 gives 1 / 2.",
        "difficulty": "High"
    },
    {
        "question_text": "If f(x) = |x - 2|, at what point is f(x) continuous but not differentiable?",
        "option_a": "x = 2",
        "option_b": "x = 0",
        "option_c": "x = -2",
        "option_d": "f(x) is differentiable everywhere",
        "correct_option": "A",
        "explanation": "The absolute value function |x - 2| creates a sharp corner (v-shape) at x = 2, making left derivative (-1) != right derivative (+1).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the derivative of sin^-1(x) with respect to cos^-1(sqrt(1 - x^2)) for 0 < x < 1?",
        "option_a": "1",
        "option_b": "-1",
        "option_c": "x",
        "option_d": "1 / sqrt(1 - x^2)",
        "correct_option": "A",
        "explanation": "Let u = sin^-1(x) and v = cos^-1(sqrt(1 - x^2)) = sin^-1(x). Thus u = v => du/dv = 1.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the derivative of log_10(x) with respect to x?",
        "option_a": "1 / (x ln(10))",
        "option_b": "1 / x",
        "option_c": "ln(10) / x",
        "option_d": "1 / (10 x)",
        "correct_option": "A",
        "explanation": "log_10(x) = ln(x) / ln(10). Differentiating with respect to x gives 1 / (x ln(10)).",
        "difficulty": "High"
    },
    {
        "question_text": "If f(x) is an even function such that integral from 0 to 3 of f(x) dx = 5, what is the value of integral from -3 to 3 of f(x) dx?",
        "option_a": "10",
        "option_b": "5",
        "option_c": "0",
        "option_d": "-10",
        "correct_option": "A",
        "explanation": "For an even function f(x), integral from -a to a of f(x) dx = 2 * integral from 0 to a of f(x) dx = 2 * 5 = 10.",
        "difficulty": "High"
    },

    # 81 - 90: Combinatorics, Binomial & Probability
    {
        "question_text": "In how many ways can 6 people sit around a circular table?",
        "option_a": "120 (5!)",
        "option_b": "720 (6!)",
        "option_c": "360",
        "option_d": "24",
        "correct_option": "A",
        "explanation": "Circular permutations of n distinct objects is (n - 1)!. For 6 people, (6 - 1)! = 5! = 120 ways.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the sum of all binomial coefficients in the expansion of (1 + x)^n?",
        "option_a": "2^n",
        "option_b": "2^(n-1)",
        "option_c": "n^2",
        "option_d": "2 n",
        "correct_option": "A",
        "explanation": "Setting x = 1 in (1 + x)^n = C(n,0) + C(n,1)x + ... + C(n,n)x^n gives C(n,0) + C(n,1) + ... + C(n,n) = 2^n.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of C(n, r) + C(n, r - 1)?",
        "option_a": "C(n + 1, r)",
        "option_b": "C(n + 1, r + 1)",
        "option_c": "C(n, r + 1)",
        "option_d": "2 C(n, r)",
        "correct_option": "A",
        "explanation": "This is Pascal's Identity: C(n, r) + C(n, r - 1) = C(n + 1, r).",
        "difficulty": "High"
    },
    {
        "question_text": "If a card is drawn at random from a well-shuffled deck of 52 cards, what is the probability that it is either a King or a Heart?",
        "option_a": "4 / 13 (16 / 52)",
        "option_b": "17 / 52",
        "option_c": "1 / 4",
        "option_d": "9 / 26",
        "correct_option": "A",
        "explanation": "P(King) = 4/52, P(Heart) = 13/52, P(King and Heart) = 1/52. P(King or Heart) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13.",
        "difficulty": "High"
    },
    {
        "question_text": "A coin is tossed 4 times. What is the probability of obtaining at least 3 heads?",
        "option_a": "5 / 16",
        "option_b": "1 / 4",
        "option_c": "3 / 8",
        "option_d": "1 / 2",
        "correct_option": "A",
        "explanation": "P(3 heads) = C(4,3)(1/2)^4 = 4/16. P(4 heads) = C(4,4)(1/2)^4 = 1/16. Total P = 4/16 + 1/16 = 5 / 16.",
        "difficulty": "High"
    },
    {
        "question_text": "If A and B are mutually exclusive events with P(A) = 0.3 and P(B) = 0.4, what is P(neither A nor B)?",
        "option_a": "0.3",
        "option_b": "0.7",
        "option_c": "0.12",
        "option_d": "0.58",
        "correct_option": "A",
        "explanation": "P(A cup B) = P(A) + P(B) = 0.3 + 0.4 = 0.7. P(neither A nor B) = 1 - P(A cup B) = 1 - 0.7 = 0.3.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the sum of the series 1 + 2 + 3 + ... + 100?",
        "option_a": "5050",
        "option_b": "5000",
        "option_c": "5100",
        "option_d": "10000",
        "correct_option": "A",
        "explanation": "Sum S_n = n(n + 1)/2 = 100 * 101 / 2 = 50 * 101 = 5050.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the value of 1^2 + 2^2 + 3^2 + ... + 10^2?",
        "option_a": "385",
        "option_b": "300",
        "option_c": "505",
        "option_d": "400",
        "correct_option": "A",
        "explanation": "Sum S = n(n+1)(2n+1)/6 = 10 * 11 * 21 / 6 = 2310 / 6 = 385.",
        "difficulty": "High"
    },
    {
        "question_text": "If log_b(a) = 3 and log_c(b) = 4, what is the value of log_c(a)?",
        "option_a": "12",
        "option_b": "7",
        "option_c": "3 / 4",
        "option_d": "64",
        "correct_option": "A",
        "explanation": "By change of base rule: log_c(a) = log_b(a) * log_c(b) = 3 * 4 = 12.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the trace of the 3x3 identity matrix I_3?",
        "option_a": "3",
        "option_b": "1",
        "option_c": "0",
        "option_d": "9",
        "correct_option": "A",
        "explanation": "Trace of a matrix is the sum of its main diagonal elements. For I_3, trace = 1 + 1 + 1 = 3.",
        "difficulty": "High"
    },

    # 91 - 100: Advanced Mathematics Review
    {
        "question_text": "If a line makes equal angles alpha, beta, gamma with the coordinate axes, what is the value of cos^2(alpha) + cos^2(beta) + cos^2(gamma)?",
        "option_a": "1",
        "option_b": "3",
        "option_c": "1 / 3",
        "option_d": "1 / sqrt(3)",
        "correct_option": "A",
        "explanation": "For direction cosines of any 3D line, l^2 + m^2 + n^2 = cos^2(alpha) + cos^2(beta) + cos^2(gamma) = 1.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the angle between the lines represented by y = x and y = -x?",
        "option_a": "pi / 2 (90 degrees)",
        "option_b": "pi / 4 (45 degrees)",
        "option_c": "pi / 3 (60 degrees)",
        "option_d": "pi (180 degrees)",
        "correct_option": "A",
        "explanation": "Slopes m1 = 1, m2 = -1. m1 * m2 = 1 * (-1) = -1. Product of slopes is -1, so lines are perpendicular (90 degrees).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the derivative of e^(x^2) with respect to x?",
        "option_a": "2x * e^(x^2)",
        "option_b": "e^(x^2)",
        "option_c": "x * e^(x^2)",
        "option_d": "2 * e^(x^2)",
        "correct_option": "A",
        "explanation": "By chain rule: d/dx [e^(x^2)] = e^(x^2) * d/dx [x^2] = 2x * e^(x^2).",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the integral: integral (1 / sqrt(1 - x^2)) dx.",
        "option_a": "sin^-1(x) + C",
        "option_b": "tan^-1(x) + C",
        "option_c": "cos^-1(x) + C",
        "option_d": "sec^-1(x) + C",
        "correct_option": "A",
        "explanation": "Standard derivative of sin^-1(x) is 1 / sqrt(1 - x^2), so integral is sin^-1(x) + C.",
        "difficulty": "High"
    },
    {
        "question_text": "Evaluate the definite integral: integral from 0 to 1 of (1 / (1 + x^2)) dx.",
        "option_a": "pi / 4",
        "option_b": "pi / 2",
        "option_c": "1",
        "option_d": "pi",
        "correct_option": "A",
        "explanation": "[tan^-1(x)] from 0 to 1 = tan^-1(1) - tan^-1(0) = pi/4 - 0 = pi / 4.",
        "difficulty": "High"
    },
    {
        "question_text": "If f(x) = x^3 - 3x, what are the local extrema points of f(x)?",
        "option_a": "Local max at x = -1 (val 2), Local min at x = +1 (val -2)",
        "option_b": "Local max at x = +1, Local min at x = -1",
        "option_c": "No local extrema",
        "option_d": "Local min at x = 0",
        "correct_option": "A",
        "explanation": "f'(x) = 3x^2 - 3 = 0 => x = +/- 1. f''(x) = 6x. f''(-1) = -6 < 0 (max at x = -1, f(-1) = 2). f''(1) = 6 > 0 (min at x = 1, f(1) = -2).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the probability of getting a total sum of 7 when two standard 6-sided dice are rolled?",
        "option_a": "1 / 6",
        "option_b": "5 / 36",
        "option_c": "1 / 12",
        "option_d": "7 / 36",
        "correct_option": "A",
        "explanation": "Favorable pairs for 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) -> 6 pairs. P = 6 / 36 = 1 / 6.",
        "difficulty": "High"
    },
    {
        "question_text": "What is the period of the function f(x) = sin(3x)?",
        "option_a": "2 pi / 3",
        "option_b": "2 pi",
        "option_c": "pi / 3",
        "option_d": "6 pi",
        "correct_option": "A",
        "explanation": "Standard period of sin(x) is 2 pi. Period of sin(k x) is 2 pi / k. Here k = 3, so Period = 2 pi / 3.",
        "difficulty": "High"
    },
    {
        "question_text": "If vectors A and B are such that |A| = 3, |B| = 4, and A . B = 6, what is the magnitude of their cross product |A x B|?",
        "option_a": "6 sqrt(3)",
        "option_b": "6",
        "option_c": "12",
        "option_d": "3 sqrt(3)",
        "correct_option": "A",
        "explanation": "cos(theta) = A . B / (|A||B|) = 6 / (3 * 4) = 6 / 12 = 1/2 => theta = 60 deg. sin(60) = sqrt(3)/2. |A x B| = |A||B| sin(theta) = 3 * 4 * (sqrt(3)/2) = 6 sqrt(3).",
        "difficulty": "High"
    },
    {
        "question_text": "What is the equation of the line passing through (1, 2) with slope m = 3?",
        "option_a": "3x - y - 1 = 0",
        "option_b": "3x - y + 1 = 0",
        "option_c": "x - 3y + 5 = 0",
        "option_d": "3x + y - 5 = 0",
        "correct_option": "A",
        "explanation": "y - y1 = m(x - x1) => y - 2 = 3(x - 1) => y - 2 = 3x - 3 => 3x - y - 1 = 0.",
        "difficulty": "High"
    }
]
