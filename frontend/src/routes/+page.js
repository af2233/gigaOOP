import 'dotenv/config';

/** @type {import('./$types').PageLoad} */

export async function load() {
    const res = await fetch(`${process.env.BASE_URL}/courses`);
    if (res.ok){
        const courses = await res.json();
        console.log(courses)
        return {
            courses
        };
    }
    
}
