/** @type {import('./$types').PageLoad} */
export async function load() {

    return {
        courses: [
            {
                title: "Python",
                description: "Learn the basics of Python programming."
            },
            {
                title: "Java",
                description: "Master the fundamentals of Java."
            },
            {
                title: "C++",
                description: "Explore the world of C++ programming."
            }
        ]
    };
}