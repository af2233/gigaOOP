<script>
	// @ts-nocheck
	/** @type {import('./$types').ActionData} */
	export let form;
	import { fade } from 'svelte/transition';

	let errorVisible = false;
	let errorMessage = '';

	if (form?.mailAlreadyExists) {
		errorMessage = 'Email already exists!';
		errorVisible = true;
		setTimeout(() => {
			errorVisible = false;
		}, 3000); // Сообщение исчезнет через 3 секунды
	}

	function hideError() {
		errorVisible = false;
	}
</script>

<style type="text/scss">
	section{
		width: 100%;
		height: 100%;
		background-color: #f5f5f5;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.form{
		background-color: #fff;
		padding: 90px 0;
		max-width: 470px;
		width: 100%;
		border-radius: 20px;
		display: flex;
		justify-content: center;
	}

	.form__content{
		max-width: 320px;
		width: 100%;
	}
	.form__title{
		font-weight: 600;
		margin-bottom: 40px;
		text-align: center;
	}
	.form__label{
		display: flex;
		flex-direction: column;
		gap: 4px;
		& p{
			font-size: 16px;
		}
	}
	.form__input{
		display: block;
		width: 100%;
		border: 1px solid #dadada;
		height: 50px;
		border-radius: 10px;
		padding: 0 15px;
		font-size: 18px;
	}

	.input-group{
		display: flex;
		flex-direction: column;
		gap: 10px;
		margin-bottom: 30px;
	}

	.btn-group{
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.btn{
		cursor: pointer;
		height: 50px;
		border-radius: 10px;
		color: #fff;
		background-color: #F9E72D;
		font-weight: 600;
		font-size: 16px;
		transition: .3s;
		&:hover{
			background-color: rgba(0, 0, 0, 0.85);
			color: #fff;
		}
	}
	.btn_register{
		border: 2px solid rgba(0, 0, 0, 0.85);
		color: rgba(0, 0, 0, 0.85);
		background-color: #fff;
	}
	.error{
		color: #fff;
		background-color: #ed4337;
		padding: 30px 10px;
		margin-top: 20px;
		border-radius: 10px;
		font-size: 18px;
		text-align: center;
	}

</style>

<section>
	<div class="form">
		<div class="form__content">
			<h2 class="form__title">Enter your profile</h2>
			<form method="POST" on:input={hideError}>
				<div class="input-group">
					<label class="form__label">
						<p>Email</p>
						<input name="email" type="email" class="form__input" value={form?.email ?? ''} required>
					</label>
					<label class="form__label">
						<p>Password</p>
						<input name="password" type="password" class="form__input" required>
					</label>
				</div>
				<div class="btn-group">
					<button formaction="?/login"  class="btn">Sign in</button>
					<button formaction="?/register" class="btn btn_register">Create an account</button>
				</div>
			</form>
			{#if errorVisible}
                <p class="error" in:fade={{ duration: 500 }} out:fade={{ duration: 500 }}>Email already exists!</p>
            {/if}
		</div>
	</div>
</section>
