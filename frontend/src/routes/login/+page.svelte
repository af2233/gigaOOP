<script>
// @ts-nocheck


	/** @type {import('./$types').ActionData} */
	export let form;
</script>


<form method="POST" action="?/register">
    <label>
		name
		<input name="name" type="text">
	</label>
    <br>
	<label>
		Email
		<input name="email" type="email">
	</label>
    <br>
	<label>
		Password
		<input name="password" type="password">
	</label>
    <br>    
	<button>register</button>
</form>

{#if form?.message}
	<p>Successfully logged in! Welcome back, {form?.message}</p>
{/if}

