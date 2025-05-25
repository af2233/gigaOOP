import { error } from '@sveltejs/kit';
import 'dotenv/config';

/** @type {import('./$types').PageLoad} */

export async function load({ params, url }) {
    const courseId = Number(params.coursePage);
    const courseTitle = url.searchParams.get('title');
    const res = await fetch(`${process.env.BASE_URL}/themes/`);

    if (res.ok) {
        const themes = await res.json();

        // Фильтруем темы по course_id
        const filteredThemes = themes.filter(theme => theme.course_id === courseId);
		if (filteredThemes.length === 0) {
            // Если нет данных для данного courseId, генерируем ошибку 404
            throw error(404, 'Course not found');
        }
        return {
            themes: filteredThemes,
            courseId: courseId,
            courseTitle: courseTitle,
        };
    }
	else {
        // Если fetch запрос не удался, генерируем ошибку
        throw error(res.status, 'Failed to fetch themes');
    }
}
