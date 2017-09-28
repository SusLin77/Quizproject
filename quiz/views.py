from django.shortcuts import render
from quiz.models import Quiz

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "startpage.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[question_number - 1]
	context = {
		"question_number": question_number,
		"question": question.question,
		"answer1": quetion.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"quiz": quiz,
		"quiz_number": quiz_number,
	}
	return render(request, "question.html", context)

def completed(request, quiz_number):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "completed.html", context)