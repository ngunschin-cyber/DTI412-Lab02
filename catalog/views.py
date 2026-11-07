def course_list_view(request):
    query = request.GET.get('q', '').strip()

    if query:
        courses = [
            course for course in COURSES_DATA
            if query.lower() in course['title'].lower()
            or query.lower() in course['code'].lower()
        ]
    else:
        courses = COURSES_DATA

    context = {
        'courses': courses,
        'query': query,
    }
    return render(request, 'catalog/course_list.html', context)