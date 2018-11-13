from django.shortcuts import render
from .forms import QuestionForm, TestCreateForm
from .models import *
from Result_Analysis.models import Teacher
from django.forms import formset_factory

def index(request):
    return render(request,'Test_Designing/exam.html')


def design(request):
    test_form = TestCreateForm()
    question_formset = formset_factory(QuestionForm)
    question_formset_post = question_formset(request.POST or None)


    if request.method == 'POST':

        test_form = TestCreateForm(request.POST)
        question_formset_post = question_formset(request.POST)

        if test_form.is_valid() and question_formset_post.is_valid():

            teacher = Teacher.objects.get(teacher=request.user)

            testList = test_form.save(commit=False)
            testList.teacher = teacher
            testList.save()


            questionList = QuestionSet.objects.create(question_list=testList)


            for question in question_formset_post:

                questionInstance = question.save(commit=False)
                questionInstance.question = questionList
                questionInstance.save()



        else:
            context = {
                'test_form':test_form,
                'question_formset':question_formset_post
            }
            return render(request, 'Test_Designing/exam_set.html', context)



    context = {
        'test_form': test_form,
        'question_formset': question_formset
    }
    return render(request, 'Test_Designing/exam_set.html', context)

