import { BASE_URL } from '../../api.js';
/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	const courseId = Number(params.coursePage);
	const res = await fetch(`${BASE_URL}/themes/`);
	console.log("course page msg")
    if (res.ok) {
		const themes = await res.json();
		console.log(themes);

		// Фильтруем темы по course_id
		const filteredThemes = themes.filter(theme => theme.course_id === courseId);
		return {
			themes: filteredThemes
		};
	}
}