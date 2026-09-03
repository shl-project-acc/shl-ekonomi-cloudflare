import { useEffect, useState } from 'react';

interface TypingHeroProps {
  alternate?: string;
  title: string;
  subtitle?: string;
}

export default function TypingHero({ alternate, title, subtitle }: TypingHeroProps) {
  const [displayedTitle, setDisplayedTitle] = useState('');
  const [isTitleFinished, setIsTitleFinished] = useState(false);
  const [displayedSubtitle, setDisplayedSubtitle] = useState('');
  const [isFinished, setIsFinished] = useState(false);

  useEffect(() => {
    let titleIndex = 0;
    let subtitleIndex = 0;
    let subtitleTimer: NodeJS.Timeout;
    let restartTimer: NodeJS.Timeout;
    let isMounted = true;

    const startTypingCycle = () => {
      if (!isMounted) return;

      // Reset states on cycle start
      setDisplayedTitle('');
      setDisplayedSubtitle('');
      setIsTitleFinished(false);
      setIsFinished(false);
      titleIndex = 0;
      subtitleIndex = 0;

      // 1. Type Title Character by Character
      const titleInterval = setInterval(() => {
        if (!isMounted) {
          clearInterval(titleInterval);
          return;
        }

        if (titleIndex < title.length) {
          setDisplayedTitle(title.slice(0, titleIndex + 1));
          titleIndex++;
        } else {
          clearInterval(titleInterval);
          setIsTitleFinished(true);

          // 2. Pause briefly (350ms) before typing subtitle
          subtitleTimer = setTimeout(() => {
            if (!isMounted) return;

            if (!subtitle) {
              setIsFinished(true);
              // Wait 10 seconds before looping
              restartTimer = setTimeout(startTypingCycle, 10000);
              return;
            }

            const subInterval = setInterval(() => {
              if (!isMounted) {
                clearInterval(subInterval);
                return;
              }

              if (subtitleIndex < subtitle.length) {
                setDisplayedSubtitle(subtitle.slice(0, subtitleIndex + 1));
                subtitleIndex++;
              } else {
                clearInterval(subInterval);
                setIsFinished(true);

                // 3. Setelah selesai animasi ngetik, tunggu 10 detik lalu ulangi loop terus menerus
                restartTimer = setTimeout(startTypingCycle, 10000);
              }
            }, 45);
          }, 350);
        }
      }, 70);
    };

    startTypingCycle();

    return () => {
      isMounted = false;
      clearTimeout(subtitleTimer);
      clearTimeout(restartTimer);
    };
  }, [title, subtitle]);

  return (
    <div className="flex flex-col items-center justify-center text-center">
      {/* SHL PROJECT tetap diam tanpa animasi ketik */}
      {alternate && (
        <h2 className="font-chill-round font-semibold text-3.5xl/[1.2] text-white/95 tracking-wider shadow-text md:text-5xl/[1.2]">
          {alternate}
        </h2>
      )}

      {/* Catatan Pribadi dan Artikel - Font Besar & Berkarakter */}
      <h1 className="mt-3 min-h-[4rem] font-bold font-chill-round text-4xl/[1.2] text-white tracking-widest shadow-text md:text-5.5xl/[1.2] lg:text-6xl/[1.2]">
        {displayedTitle}
        {!isTitleFinished && <span className="inline-block w-2 animate-pulse bg-white align-middle text-transparent">|</span>}
      </h1>

      {/* Subtitle = Amalan yang paling dicintai Allah... = Mengetik lalu jeda 10 detik dan loop */}
      <div className="mt-4 min-h-[2.5rem]">
        {isTitleFinished && subtitle && (
          <p className="font-medium text-sm text-white/90 tracking-wide shadow-text md:text-base lg:text-lg">
            = {displayedSubtitle}
            {!isFinished && (
              <span className="inline-block w-1.5 animate-pulse bg-white/80 align-middle text-transparent">|</span>
            )}
            {isFinished && ' ='}
          </p>
        )}
      </div>
    </div>
  );
}
