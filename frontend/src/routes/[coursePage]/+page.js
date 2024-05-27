import { BASE_URL } from '../../api.js';
import { error } from '@sveltejs/kit';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    const courseId = Number(params.coursePage);

    const res = await fetch(`${BASE_URL}/themes/`);

    if (res.ok) {
        const themes = await res.json();

        // Фильтруем темы по course_id
        const filteredThemes = themes.filter(theme => theme.course_id === courseId);

        if (filteredThemes.length === 0) {
            // Если нет данных для данного courseId, генерируем ошибку 404
            throw error(404, 'Course not found');
        }

        return {
            themes: filteredThemes
        };
    } else {
        // Если fetch запрос не удался, генерируем ошибку
        throw error(res.status, 'Failed to fetch themes');
    }
}

