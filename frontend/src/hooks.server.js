
/** @type {import('@sveltejs/kit').Handle} */

import { redirect } from '@sveltejs/kit';

export async function handle({ event, resolve }) {
    const token = event.cookies.get('token');

    console.log(`Token: ${token}`); // Логирование для отладки
    console.log(`Pathname: ${event.url.pathname}`);
    console.log(`Headers: ${JSON.stringify(event.request.headers)}`);
    
    if (!token && event.url.pathname !== '/login') {
        console.log(`Redirecting to /login from ${event.url.pathname}`);
        redirect(307, '/login');
        
    }

    return resolve(event);
}