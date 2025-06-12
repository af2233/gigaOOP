/** @type {import('./$types').PageLoad} */

export async function load() {
    const res = await fetch('http://localhost:8000/courses');
    if (res.ok){
        const courses = await res.json();
        console.log(courses)
        return {
            courses
        };
    }
    
}
