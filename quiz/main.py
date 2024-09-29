import pgzrun

WIDTH = 870
HEIGHT = 650 
TITLE = "Test Your Knowledge!"
score = 0
time_left = 10
question_file_name = "question.txt"
is_game_over = False

#boxes
marquee_box = Rect(0,0, 880, 80)
question_box = Rect(0, 0, 650,150)
timer_box = Rect(0, 0, 150, 150)
answer_box1 = Rect(0, 0, 300, 150)
answer_box2 = Rect(0, 0, 300, 150)
answer_box3 = Rect(0, 0, 300, 150)
answer_box4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 150, 330)
#numbers and lists
marquee_message = ""
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0
#box positions
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700, 270)


#functions

def draw():
    global marquee_message
    screen.clear()
    screen.fill("pink")
    screen.draw.filled_rect(marquee_box, "white")
    screen.draw.filled_rect(question_box, "white")
    screen.draw.filled_rect(timer_box, "white")
    screen.draw.filled_rect(skip_box, "white")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "sky blue")

def read_question_file():
    global question_count, questions
    q_file = open(question_file_name, "r")
    for row in q_file:
        questions.append(row)
        question_count += 1
    q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")
pgzrun.go()