/** @type {import('./$types').PageLoad} */
export async function load({ params, parent }) {
	const course = params.coursePage;
    const par = await parent()
	return {course, par};    
}