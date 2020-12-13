%<!-- % - Note: Any line starts with "%" mark is a comment line that will not be processed and could be deleted. - -->

%<!-- % ********************Quiz title part*********************************************************** -->
%<!-- % Start the quiz with a title. Title has only one line and will be processed as raw text. -->
Quiz title: Sample Quiz from Template
%<!-- % ********************Quiz title part*********************************************************** -->


%<!-- % ********************(optional) Quiz description part*************************************************** -->
%<!-- %  Quiz description will be rendered as "Quiz Instruction" on Canvas -->
Quiz description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique fermentum odio ut accumsan. Suspendisse sit amet lorem ut tellus vehicula rutrum. Integer nisi diam, tempus sed diam quis, suscipit interdum libero. Maecenas nec lacus maximus massa rhoncus hendrerit bibendum vitae ante. Sed et mauris dolor. Mauris non urna tellus. Vivamus ut lectus euismod, mattis libero non, aliquet est. Integer ut justo ut sapien tincidunt rutrum sed sed sapien. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras congue erat est, in molestie velit lobortis ac. Nulla nulla erat, egestas vel eleifend at, tincidunt sit amet massa.

%<!-- %  Images need to be hosted outside of the Canvas -->
%<!-- %  Or upload the images to the Canvas first and get the generated URL from Canvas -->
![](https://upload.wikimedia.org/wikipedia/commons/8/89/Euclid%27s_algorithm_Book_VII_Proposition_2_2.png)

Nunc at elit urna. Nullam vitae varius quam. Vivamus vitae risus metus. Donec lorem libero, pharetra ac feugiat elementum, tristique vel libero. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris auctor cursus fermentum. Donec faucibus nulla elementum, vehicula augue at, commodo nisi. Aliquam eu tellus erat. Phasellus ultrices luctus libero quis ultrices. Phasellus sapien nisl, aliquam eget leo eu, faucibus rhoncus nulla.
%<!-- % ********************Quiz description part*************************************************** -->

%<!-- % ********************(optional) Quiz options part*************************************************** -->
%<!-- % Specify whether some quiz options should be enabled by putting "true" or "false" after the option -->
Shuffle answers: true
Show correct answers: true
One question at a time: true
Can't go back: true
%<!-- % ********************Quiz options part*************************************************** -->


%<!-- % ********************Quiz Title/Description/Options need to be defined before questions!!************* -->


%<!-- % ********************Start Defining Questions*************************************************** -->
%<!-- % ********************Sample Question (General Parameters and Multi-choice Example)********* -->
%<!-- % (optional) Title of the question -->
Title: Multi-choices question
%<!-- % (optional) Points of the question -->
Points: 2
%<!-- % (REQUIRED) Description of the question, start the line with "Q.". -->
%<!-- % Description of the question could have multiple lines/paragraphs, Please use an empty line to separate the paragraphs -->
Q.  What is 2+3?

Think about the addition example we had learned previously

%<!-- % (optional) Feedbacks for answer of the question. -->
... General question feedback. (For example, "continue to next question")
+   Feedback for correct answer. (For example, "congratulations" )
~   Feedback for incorrect answer. (For example, "try next time" )
%<!-- % For Multi-choice Example, list each answer as a line that start with  -->
%<!-- %  a letter followed by a closing parenthesis and one or more spaces or tabs ("a) ") -->
a)  6
... Feedback for this particular answer.(For example, "should be smaller" )
b)  1
... Feedback for this particular answer.(For example, "should be larger ")
%<!-- % The correct choice is designated with an asterisk ("*c) "). -->
*c) 5
... Feedback for this particular answer.(For example, "congratulations" )
%<!-- % ********************Sample Question (General Parameters and Multi-choice Example)********* -->

%<!-- % ********************Sample Question (Multi-answers question)******************************** -->
Title: Multi-answers question
Points: 1
Q.  Which of the following are dinosaurs?
%<!-- % use [] or [ ] for incorrect answers and [*] for correct answers. -->
[ ] Woolly mammoth
[*] Tyrannosaurus rex
[*] Triceratops
[ ] Smilodon fatalis
%<!-- % ********************Sample Question (Multi-answers question)******************************** -->

%<!-- % ********************Example to add a text regions****************************************** -->
Text title:  Instructions about the next questions
Text:  General comments about the next questions.
%<!-- % ********************Example to add a text regions****************************************** -->

%<!-- % ********************Sample Question (Numerical Questions)******************************** -->
Title: Numerical question 1
Points: 3
Q.  What is the square root of 2?
%<!-- % use an equals sign followed by one or more spaces or tabs followed by the numerical answer -->
%<!-- % answers can be a correct answer with a specified acceptable margin of error <ans> +- <margin>    -->
=   1.4142 +- 0.0001

Title: Numerical question 2
Points: 3
Q.  What is the cube root of 2?
%<!-- % answers can be a range of the form [<min>, <max>] -->
=   [1.2598, 1.2600]

Title: Numerical question 3
Points: 3
Q.  What is 2+4? (dup?)
%<!-- % answers can be exact number -->
=   6
%<!-- % ********************Sample Question (Numerical Questions)******************************** -->


%<!-- % ********************Sample Question (Fill-in-the-blank Questions)******************************** -->
Title: Short-answer (fill-in-the-blank) questions
Points: 3
Q.  Who lives at the North Pole?
%<!-- % use <> followed by one or more spaces or tabs followed by a possible answer -->
<>   Santa
<>   Santa Claus
<>   Father Christmas
<>   Saint Nicholas
<>   Saint Nick
%<!-- % ********************Sample Question (Fill-in-the-blank Questions)******************************** -->


%<!-- % ********************Sample Question (Essay question)******************************** -->
Title: (Essay questions)
Points: 10
Q.  Write an essay.
%<!-- % Use a sequence of three or more underscores at the next line of question description to mark-->
%<!-- % this question as the essay question-->
____
%<!-- % ********************Sample Question (File Upload)******************************** -->
Title: (File Upload)
Points: 10
Q. Upload a file.
^^^^
%<!-- % Use a sequence of three or more carets at the next line of question description to mark-->
%<!-- % this question as the file upload question-->

%<!-- % ********************Sample Question (Fill-in-multiple-blanks Questions)******************************** -->
Title: Fill in multiple blanks
Points: 10
Q.  In the box below, every place you want to show an answer box, type a reference word (no spaces) surrounded by brackets(i.e. "Roses are [color1], violets are [color2]")
%<!-- % use <> followed by spaces and [reference word] for answers of each blank marked by the reference word -->
<>    [color1]    red
<>    [color1]    RED
<>    [color1]    Red
<>    [color2]    BLUE
%<!-- % ********************Sample Question (Fill-in-multiple-blanks Questions)******************************** -->


%<!-- % ********************Sample Question (Multiple Dropdowns Questions)******************************** -->
Title: Cache and Memory (Multiple dropdown example)
Points: 10
Q. Consider a word-addressable (1 word = 4 bytes) computer with a main memory of 16 MB (2^24). The cache is capable of storing a total of 128 B of data and a block size of 16 bytes. 

 The physical memory address is  [Addr_len] bits.

 As a 4-way set associative cache:

 - the tag is [tag] bits

 - the set index is [set] bits

 - the block offset is [offset] bits

What is the lowest address in the cache block, when the address 0x17634E is brought into the cache? [lowest_address]

%<!-- % use { } followed by spaces and [reference word] for incorrect answers of each blank marked by the reference word -->
%<!-- % use {*} for correct answers. -->
{*}   [Addr_len]  22
{ }   [Addr_len]  24
{ }   [Addr_len]   23
{ }   [Addr_len]  26
{*}   [tag]  19
{ }   [tag]   20
{ }   [tag]   21
{ }   [tag]   22
{ }   [tag]   28
{*}   [set]  1
{ }   [set]   0
{ }   [set]   2
{ }   [set]   3
{ }   [set]   4
{ }   [offset]  1
{ }   [offset]   0
{*}   [offset]   2
{ }   [offset]   3
{ }   [offset]   4
{ }   [offset]   5
{ }   [lowest_address]   0x17634E
{*}   [lowest_address]   0x17634C
{ }   [lowest_address]   0x01053F
{ }   [lowest_address]   0x010538
%<!-- % ********************Sample Question (Multiple Dropdowns Questions)******************************** -->

%<!-- % ********************Using Question Group ***************************************************** -->
%<!-- Use keyword "GROUP" to mark the start of a group and "END_GROUP" to mark the end of a group -->
GROUP
%<!-- For each group, you could specify how many question will be picked and what are the points for the picked question -->
pick: 2
points per question: 3

%<!-- Questions with the same descriptions can be repeated as long as they have a different title -->
Title: Test1
Q.  A question.
*a) true
b)  false

Title: Test2
Q.  A question.
a) true
*b)  false

Q.  Which of the following are cloud service providers?
[ ] EVGA
[*] Azure
[*] AWS
[ ] LG

Q.  What is the cube root of 3?
=   [1.4420, 1.4425]
END_GROUP
%<!-- % ********************Using Question Group ***************************************************** -->