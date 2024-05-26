import { BASE_URL } from '../../api.js';

/** @type {import('./$types').PageLoad} */
export async function load({ params, url }) {
    const courseId = Number(params.coursePage);
    const courseTitle = url.searchParams.get('title');
    const res = await fetch(`${BASE_URL}/themes/`);

    if (res.ok) {
        const themes = await res.json();

        // Фильтруем темы по course_id
        const filteredThemes = themes.filter(theme => theme.course_id === courseId);
        return {
            themes: filteredThemes,
            courseId: courseId,
            courseTitle: courseTitle,
        };
    }
    return { themes: [], courseId: courseId, courseTitle: courseTitle }; // на случай, если запрос не удался
}