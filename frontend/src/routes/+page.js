import 'dotenv/config';

/** @type {import('./$types').PageLoad} */

export async function load() {
    const res = await fetch(`${process.env.COURSES_URL}`);
    if (res.ok){
        const courses = await res.json();
        console.log(courses)
        return {
            courses
        };
    }
    
}
