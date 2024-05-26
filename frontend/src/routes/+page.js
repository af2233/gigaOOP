import { BASE_URL } from '../api.js';
/** @type {import('./$types').PageLoad} */
export async function load() {
    const res = await fetch(`${BASE_URL}/courses`);
    if (res.ok){
        const courses = await res.json();
        console.log(courses)
        return {
            courses
        };
    }
    
}